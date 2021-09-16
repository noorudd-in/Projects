import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    lottie_welcome = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_q5qeoo3q.json")
    st_lottie(lottie_welcome, key="welcome")
    show_predict_page()

else:
    lottie_hello = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_zlrpnoxz.json")
    st_lottie(lottie_hello, key="hello")
    show_explore_page()
