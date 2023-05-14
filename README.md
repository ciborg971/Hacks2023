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

## Setup the streamlit widget

from project root

``cd st_tez_did``

``cd src/st_tez_did/frontend``

``npm install``

``cd -``

path should be HACKS2023/st_tez_did, and install it via

``pip3 install -e .``

Congratulation, you have now an awesome library to use Taquito/Temple wallet from Streamlit

You can test it with 
``streamlit run src/st_tez_did/__init__.py``

## Requirement

- A Temple wallet

## Launch with launch script

``chmod +x ./launch.sh``

``./launch.sh``

## Launch manualy
### Launch didkit-http

from root of repository

./didkit/target/debug/didkit-http &

example output : ``2023-05-13T05:41:13.207339Z  INFO didkit_http: listening on 127.0.0.1:3000``

note the port number used

### Streamlit

from root of repository

``streamlit run Authentification.py``

## Beyond the demo

    - Generate an issuer_key

``./didkit/target/debug/didkit generate-ed25519-key > issuer_key.jw``

    - Generate a DID:Key document

``did=$(./didkit/target/debug/didkit key-to-did -k issuer_key.jwk )``
``printf 'DID: %s\n\n' "$did``

output ``DID: did:key:z6MkjV9Ds7F3Qkbz1rAo9Zsq2C8SNzP8QCeQ4JSonZdjt9L``

    - Generate verification method

``verification_method=$(./didkit/target/debug/didkit key-to-verification-method -k issuer_key.jwk``

``didkit: key-to-verification-method should be used with method pattern optio``

``printf 'verificationMethod: %s\n\n' "$verification_method"``
``verificationMethod:did:key:z6MkjV9Ds7F3Qkbz1rAo9Zsq2C8SNzP8QCeQ4JSonZdjt9La#z6MkjV9Ds7F3Qkbz1rAo9Zsq2C8SNzP8QCeQ4JSonZdjt9La``

    - Launch didkit server with issuer key

``./didkit/target/debug/didkit-http -p 3000 -k issuer_key.jwk & pid=$!``

## Tools

[Didkit : create, update and delete DID related information](https://github.com/spruceid/didkit)

[Did:tz : create, update and delete DID related information with didkit on Rezos](https://github.com/spruceid/did-tezos)

[Temple : wallet tezos](https://templewallet.com)

[Taquito : bibliothèque JS pour discuter avec le wallet](https://tezostaquito.io)
[Exemple JS : Taquito + Temple + didkit](https://github.com/spruceid/didkit-tezos-wallet-example/tree/main)