# Hacks2023

## Python dependencies

pip install watchdog streamlit

## Setup didkit
### Setup Rust

Follow Rustup guide to setup the Rust toolachain
[Rustup](https://rustup.rs)

### Compile didkit
check that ssi and didkit folder exist and are not empty

cd didkit
cargo build

### Launch didkit-http
from root of repository
./didkit/target/debug/didkit-http
example output 2023-05-13T05:41:13.207339Z  INFO didkit_http: listening on 127.0.0.1:3000
take note of the port number used

## Streamlit
