use dialoguer::{theme::ColorfulTheme, Confirm, Input, Select};
use fake::faker::address::en::CityName;
use fake::faker::internet::en::SafeEmail;
use fake::faker::internet::en::Username;
use fake::faker::name::en::{FirstName, LastName};
use fake::faker::phone_number::en::PhoneNumber;
use fake::{Dummy, Fake, Faker};
use indicatif::{ProgressBar, ProgressStyle};
use mongodb::bson;
use mongodb::bson::{doc, Document};
use mongodb::{Client, Collection, Database};
use rayon::prelude::*;
use serde::Serialize;
use std::fs::File;
use std::io::Write;
use toml;

#[derive(Dummy, Serialize, Clone)]
struct User {
    #[dummy(faker = "FirstName()")]
    firstname: String,
    #[dummy(faker = "LastName()")]
    lastname: String,
    #[dummy(faker = "Username()")]
    username: String,
    #[dummy(faker = "CityName()")]
    city: String,
    #[dummy(faker = "(18..80)")]
    age: u8,
    #[dummy(faker = "SafeEmail()")]
    email: String,
    #[dummy(faker = "PhoneNumber()")]
    phone_number: String,
}

fn generate_users(chunk_size: u64) -> Vec<User> {
    (0..chunk_size)
        .into_par_iter()
        .map(|_| {
            let user: User = Faker.fake();
            //user.email=format!("{}.{}@gmail.com", user.firstname.to_lowercase(), user.lastname.to_lowercase());
            user
        })
        .collect()
}

async fn send_to_postgres(
    users: Vec<User>,
    database_url: &str,
    table_name: &str,
) -> Result<(), tokio_postgres::Error> {
    // Connect to PostgreSQL
    let (client, connection) = tokio_postgres::connect(database_url, tokio_postgres::NoTls).await?;
    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprintln!("connection error: {}", e);
        }
    });

    // Prepare the statement
    let statement = client
        .prepare(&format!(
            "INSERT INTO {} (firstname, lastname, username, city, age, email, phone_number) VALUES ($1, $2, $3, $4, $5, $6, $7)",
            table_name
        ))
        .await?;

    // Execute the statement for each user
    for user in users {
        client
            .execute(
                &statement,
                &[
                    &user.firstname,
                    &user.lastname,
                    &user.username,
                    &user.city,
                    &(user.age as i32), // PostgreSQL expects age as an integer
                    &user.email,
                    &user.phone_number,
                ],
            )
            .await?;
    }

    Ok(())
}

async fn send_to_mongodb(
    users: Vec<User>,
    database_name: &str,
    collection_name: &str,
) -> Result<(), mongodb::error::Error> {
    // Connect to MongoDB
    let client = Client::with_uri_str("mongodb://localhost:27017/").await?;
    let db: Database = client.database(database_name);
    let collection: Collection<Document> = db.collection(collection_name);

    // Convert users to BSON documents and insert into collection
    let user_documents: Vec<Document> = users
        .into_iter()
        .map(|user| bson::to_document(&user).unwrap())
        .collect();

    // Insert documents into collection
    collection.insert_many(user_documents, None).await?;

    Ok(())
}

#[tokio::main]
async fn main() {
    // Prompt the user for the number of datasets to generate
    let num_datasets: u64 = loop {
        let input: String = Input::with_theme(&ColorfulTheme::default())
            .with_prompt("Enter the number of datasets to generate (multiples of 10000, default: 1 million):")
            .default(1_000_000.to_string())
            .interact_text()
            .unwrap_or_else(|e| {
                eprintln!("Failed to interact with user: {}", e);
                std::process::exit(1);
            });

        match input.parse::<u64>() {
            Ok(value) if value % 10_000 == 0 => break value,
            Ok(_) => println!("Please enter a number that is a multiple of 10000."),
            Err(_) => println!("Please enter a valid number."),
        }
    };

    let chunk_size = 10_000;
    let num_chunks = num_datasets / chunk_size;

    let progress_bar = ProgressBar::new(num_chunks);
    progress_bar.set_style(
        ProgressStyle::default_bar().template("[{elapsed_precise}] [{bar:40}] {pos}/{len} chunks"),
    );

    let users: Vec<User> = (0..num_chunks)
        .into_par_iter()
        .inspect(|_| progress_bar.inc(1))
        .flat_map(|_| generate_users(chunk_size))
        .collect();

    progress_bar.finish_and_clear();

    let save_file = Confirm::with_theme(&ColorfulTheme::default())
        .with_prompt("Do you want to save the generated dataset to a file?")
        .default(true)
        .interact()
        .unwrap_or_else(|e| {
            eprintln!("Failed to interact with user: {}", e);
            std::process::exit(1);
        });
    if save_file {
        let toml_data = toml::to_string(&users).expect("Failed to serialize data to TOML");

        let mut file = File::create("fake_dataset.toml").expect("Failed to create file");
        file.write_all(toml_data.as_bytes())
            .expect("Failed to write to file");
    }

    let selection = Select::with_theme(&ColorfulTheme::default())
        .with_prompt("Do you want to send the data to MongoDB, PostgreSQL, both, or neither?")
        .default(0)
        .items(&["MongoDB", "PostgreSQL", "Both", "Neither"])
        .interact_opt()
        .unwrap_or_else(|e| {
            eprintln!("Failed to interact with user: {}", e);
            std::process::exit(1);
        });

    match selection {
        Some(choice) => {
            let send_to_mongodb_bool = choice == 0 || choice == 2;
            let send_to_postgres_bool = choice == 1 || choice == 2;

            // If user chooses to send to MongoDB
            if send_to_mongodb_bool {
                match send_to_mongodb(users.clone(), "your_database_name", "your_collection_name")
                    .await
                {
                    Ok(_) => {
                        println!("Data sent to MongoDB successfully");
                    }
                    Err(err) => {
                        eprintln!("Failed to send data to MongoDB: {}", err);
                    }
                }
            }

            if send_to_postgres_bool {
                if let Err(err) = send_to_postgres(
                    users,
                    "postgresql://username:password@localhost/database",
                    "users",
                )
                .await
                {
                    eprintln!("Failed to send data to PostgreSQL: {}", err);
                }
            }
        }
        None => {
            println!("No option selected. Exiting...");
        }
    }
}
