use std::io::{Read, Write};
use std::net::TcpStream;
use std::thread;
use rand::Rng;

fn main() {
    let mut handles = vec![];

    for _ in 0..5000 {
        let handle = thread::spawn(|| {
            let mut stream = TcpStream::connect("127.0.0.1:7878").unwrap();

            // Generate a random word
            let word: String = rand::thread_rng()
                .sample_iter(&rand::distributions::Alphanumeric)
                .take(10)
                .map(char::from)
                .collect();

            let request = format!("Sending: {}", word);
            stream.write(request.as_bytes()).unwrap();
            stream.flush().unwrap();

            let mut buffer = [0; 512];
            stream.read(&mut buffer).unwrap();

            println!("Received: {}", String::from_utf8_lossy(&buffer[..]));
        });

        handles.push(handle);
    }

    // Wait for all threads to finish
    for handle in handles {
        handle.join().unwrap();
    }
}
