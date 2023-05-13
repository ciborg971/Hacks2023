# Hacks2023

## Python dependencies

``pip install watchdog streamlit``

## Setup didkit
### Setup Rust

Follow [Rustup](https://rustup.rs) guide to setup the Rust toolchain

### Compile didkit
check that ssi and didkit folder exist and are not empty

``cd didkit``

``cargo build``

### Requirement

- A Temple wallet

### Launch didkit-http

from root of repository

``./didkit/target/debug/didkit-http
example output 2023-05-13T05:41:13.207339Z  INFO didkit_http: listening on 127.0.0.1:3000
``

note of the port number used

## Streamlit

from root of repository

``streamlit run Authentification.py``

## Tools

[Didkit : create, update and delete DID related information](https://github.com/spruceid/didkit)

[Did:tz : create, update and delete DID related information with didkit on Rezos](https://github.com/spruceid/did-tezos)

[Temple : wallet tezos](https://templewallet.com)

[Taquito : bibliothèque JS pour discuter avec le wallet](https://tezostaquito.io)
[Exemple JS : Taquito + Temple + didkit](https://github.com/spruceid/didkit-tezos-wallet-example/tree/main)