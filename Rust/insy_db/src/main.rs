use std::fs::File;
use std::io::{self, Read};
use toml;
use serde::Deserialize;
use serde::Serialize; // Add this import
use mongodb::{Client, Database, Collection};
use mongodb::bson::{doc, Document};
use mongodb::bson;

#[derive(Deserialize)]
struct User {
    firstname: String,
    lastname: String,
    username: String,
    city: String,
    age: u8,
    email: String,
    phone_number: String,
}

fn read_toml_file(file_path: &str) -> Result<Vec<User>, toml::de::Error> {
    let mut file = File::open(file_path)?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    let users: Vec<User> = toml::from_str(&content)?;
    Ok(users)
}

fn send_to_mongodb(users: Vec<User>, database_name: &str, collection_name: &str) -> Result<(), mongodb::error::Error> {
    // Connect to MongoDB
    let client = Client::with_uri_str("mongodb://localhost:27017/")?;
    let db: Database = client.database(database_name);
    let collection: Collection<Document> = db.collection(collection_name);

    // Convert users to BSON documents and insert into collection
    let user_documents: Vec<Document> = users.into_iter().map(|user| {
        bson::to_document(&user).unwrap()
    }).collect();

    collection.insert_many(user_documents, None)?;

    Ok(())
}

fn main() {
    let file_path = "fake_dataset.toml";
    let database_name = "your_database_name";
    let collection_name = "your_collection_name";

    // Read data from TOML file
    let users = match read_toml_file(file_path) {
        Ok(users) => users,
        Err(err) => {
            eprintln!("Error reading TOML file: {}", err);
            return;
        }
    };

    // Send data to MongoDB
    if let Err(err) = send_to_mongodb(users, database_name, collection_name) {
        eprintln!("Failed to send data to MongoDB: {}", err);
    } else {
        println!("Data successfully sent to MongoDB");
    }
}
