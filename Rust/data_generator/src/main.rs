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
use std::time::Instant;

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
    let (mut client, connection) =
        tokio_postgres::connect(database_url, tokio_postgres::NoTls).await?;
    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprintln!("connection error: {}", e);
        }
    });

    let check_table_exists_query = format!(
        "CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            username VARCHAR(255),
            city VARCHAR(255),
            age INTEGER,
            email VARCHAR(255),
            phone_number VARCHAR(255)
        )",
        table_name
    );
    client.execute(&check_table_exists_query, &[]).await?;

    let transaction = client.transaction().await?;

    let progress_bar = ProgressBar::new(users.len() as u64);
    progress_bar.set_style(
        ProgressStyle::default_bar()
            .template("[{elapsed_precise}] [{bar:40}] {pos}/{len} PostgreSQL insertions ({eta})")
            .progress_chars("=> "),
    );

    let statement = transaction
        .prepare(&format!(
            "INSERT INTO {} (firstname, lastname, username, city, age, email, phone_number) VALUES ($1, $2, $3, $4, $5, $6, $7)",
            table_name
        ))
        .await?;

    for user in users {
        transaction
            .execute(
                &statement,
                &[
                    &user.firstname,
                    &user.lastname,
                    &user.username,
                    &user.city,
                    &(user.age as i32),
                    &user.email,
                    &user.phone_number,
                ],
            )
            .await?;

        progress_bar.inc(1);
    }

    transaction.commit().await?;

    progress_bar.finish_with_message("Insertions completed");

    Ok(())
}

async fn send_to_mongodb(
    users: Vec<User>,
    database_name: &str,
    collection_name: &str,
    use_insert_many: bool,
) -> Result<(), mongodb::error::Error> {
    let client = Client::with_uri_str("mongodb://localhost:27017/").await?;
    let db: Database = client.database(database_name);
    let collection: Collection<Document> = db.collection(collection_name);

    if !use_insert_many {
        let progress_bar = ProgressBar::new(users.len() as u64);
        progress_bar.set_style(
            ProgressStyle::default_bar()
                .template("[{elapsed_precise}] [{bar:40}] {pos}/{len} MongoDB insertions ({eta})")
                .progress_chars("=> "),
        );

        for user in users {
            let user_document = bson::to_document(&user).unwrap();
            collection.insert_one(user_document, None).await?;
            progress_bar.inc(1);
        }

        progress_bar.finish_with_message("Insertions completed");
    } else {
        let user_documents: Vec<Document> = users
            .into_iter()
            .map(|user| bson::to_document(&user).unwrap())
            .collect();

        collection.insert_many(user_documents, None).await?;
    }

    Ok(())
}

#[tokio::main]
async fn main() {
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
        ProgressStyle::default_bar()
            .template("[{elapsed_precise}] [{bar:40}] {pos}/{len} chunks generated ({eta})"),
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
            let mut use_insert_many = true;

            if send_to_mongodb_bool {
                use_insert_many = Confirm::with_theme(&ColorfulTheme::default())
                    .with_prompt("Do you want to take advantage of MongoDB insert_many? (gives MongoDB an unfair advantage)")
                    .default(true)
                    .interact()
                    .unwrap_or_else(|e| {
                        eprintln!("Failed to interact with user: {}", e);
                        std::process::exit(1);
                    });
            }

            if send_to_mongodb_bool {
                let start = Instant::now();
                match send_to_mongodb(users.clone(), "data", "users", use_insert_many).await {
                    Ok(_) => {
                        let duration = start.elapsed();
                        println!("Data sent to MongoDB successfully in {:?}", duration);
                    }
                    Err(err) => {
                        eprintln!("Failed to send data to MongoDB: {}", err);
                    }
                }
            }

            if send_to_postgres_bool {
                let start = Instant::now();
                match send_to_postgres(users, "postgresql://user:password@localhost/data", "users")
                    .await
                {
                    Ok(_) => {
                        let duration = start.elapsed();
                        println!("Data sent to PostgreSQL successfully in {:?}", duration);
                    }
                    Err(err) => {
                        eprintln!("Failed to send data to PostgreSQL: {}", err);
                    }
                }
            }
        }
        None => {
            println!("No option selected. Exiting...");
        }
    }
}
