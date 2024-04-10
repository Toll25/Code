use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};
use std::thread;
use rand::Rng;
use rayon::prelude::*;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    // Use a thread pool to handle connections
    listener.incoming().par_bridge().for_each(|stream| {
        match stream {
            Ok(stream) => {
                handle_client(stream);
            }
            Err(e) => {
                println!("Error: {}", e);
            }
        }
    });
}

fn handle_client(mut stream: TcpStream) {
    let mut buffer = [0; 512];
    stream.read(&mut buffer).unwrap();

    println!("Received: {}", String::from_utf8_lossy(&buffer[..]));

    // Generate a random word
    let word: String = rand::thread_rng()
        .sample_iter(&rand::distributions::Alphanumeric)
        .take(10)
        .map(char::from)
        .collect();

    let response = format!("Random word: {}", word);
    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}
