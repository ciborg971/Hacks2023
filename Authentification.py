import streamlit as st
import numpy as np
import pandas as pd
import time
import requests
import datetime
from st_tez_did import st_tez_did

st.title("Tezos Graduate")

issuer_did = "did:key:z6MkjV9Ds7F3Qkbz1rAo9Zsq2C8SNzP8QCeQ4JSonZdjt9La"
didkit_url = "http://localhost:3000"

value = st_tez_did('TezosGraduate', 'mainnet')
if value is not None:
    st.session_state["WalletID"] = "did:pkh:tz:" + value["pub"]

if "WalletID" not in st.session_state:
    st.write("### Click on the button above to connect your wallet")

if "WalletID" in st.session_state and 'CV' not in st.session_state:
    st.session_state['CV'] = dict()
    st.session_state["CV"]["School"] = []
    st.session_state["CV"]["Exp"] = []
    st.session_state["CV"]["Cert"] = []
    st.session_state["CV"]["State"] = "Empty"
    st.session_state["CV"]["Page"] = 0
    st.write("### No CV found, go to Create my CV")

if 'CV' in st.session_state and st.session_state['CV']["State"] != "Empty" and st.session_state['WalletID'] is not None :
    st.write("Waiting for TezosGraduate validation")
    time.sleep(20.0)
    st.write("TezosGraduate has validated your CV")
    date_time = datetime.datetime.now()
    date_time_str = date_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    unsigned_cv = {
        "@context": "https://www.w3.org/2018/credentials/v1",
        "id": "http://example.org/credentials/3731",
        "type": ["VerifiableCredential", "AlumniCredential"],
        "issuer": issuer_did,
        "issuanceDate": date_time_str,
        "credentialSubject": {
            "id": st.session_state["WalletID"],
            "CV": st.session_state["CV"],
        }
    }

    headers = {'content-type': 'application/json'}
    payload = {
        "credential": unsigned_cv,
        "options": {
            "verificationMethod": "did:key:z6MkjV9Ds7F3Qkbz1rAo9Zsq2C8SNzP8QCeQ4JSonZdjt9La#z6MkjV9Ds7F3Qkbz1rAo9Zsq2C8SNzP8QCeQ4JSonZdjt9L",
            "proofPurpose": "assertionMethod"
        }
    }

    r = requests.post(didkit_url + "/issue/credentials", data=payload, headers=headers)
    st.write(r)
    #print(r)
    if r == "<Response [400]>":
        st.balloons()