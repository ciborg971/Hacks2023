import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Tezos Graduate")

if st.button('Connect your wallet') :
    st.session_state["WalletID"] = "098765432"

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

if 'CV' in st.session_state and st.session_state['CV']["State"] != "Empty" :
    st.write("Waiting for TezosGraduate validation")
    time.sleep(20.0)
    st.write("TezosGraduate has validated your CV")
    st.balloons()