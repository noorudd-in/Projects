import streamlit as st
import pickle
import numpy as np
import pandas as pd


def load_model():
    with open('./model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]


def show_predict_page():
    st.title("AQI prediction")
    st.write("""Input info. to predict AQI""")
    PM2_5 = st.number_input("PM2.5 (Usually ranges from 0.1 to 120)", min_value=0.0, max_value=950.0, step=0.01, format="%.2f")
    NO2 = st.number_input("NO2 (Usually ranges from 0.01 to 60)", min_value=0.0, max_value=362.0, step=0.01, format="%.2f")
    CO = st.number_input("CO (Usually ranges from 0 to 3)", min_value=0.0, max_value=1756.0, step=0.01, format="%.2f")
    SO2 = st.number_input("SO2 (Usually ranges from 0.01 to 25)", min_value=0.0, max_value=194.0, step=0.01, format="%.2f")
    O3 = st.number_input("O3 (Usually ranges from 0.01 to 65)", min_value=0.0, max_value=258.0, step=0.01, format="%.2f")

    ok = st.button("Calculate AQI")
    if ok:
        X = np.array([[PM2_5, NO2, CO, SO2, O3]])
        X = X.astype(float)
        AQI = regressor.predict(X)

        if round(AQI[0], 0) >= 0 and round(AQI[0], 0) <= 55:
            st.subheader(f"The estimated AQI is Good")
        elif round(AQI[0], 0) >= 56 and round(AQI[0], 0) <= 100:
            st.subheader(f"The estimated AQI is Satisfactory")
        elif round(AQI[0], 0) >= 101 and round(AQI[0], 0) <= 200:
            st.subheader(f"The estimated AQI is Moderate")
        elif round(AQI[0], 0) >= 201 and round(AQI[0], 0) <= 300:
            st.subheader(f"The estimated AQI is Poor")
        else:
            st.subheader(f"The estimated AQI is Severe")

    st.text("")
    st.text("")
    st.text("")
    link = '[Fork the source code on Github](https://github.com/noor12401/Projects/tree/main/AQI)'
    st.markdown(link, unsafe_allow_html=True)
    st.text("")
    st.write("Contributors")
    st.write("[Nooruddin](https://www.linkedin.com/in/nooruddin-shaikh)")
    st.write("[Karthik](https://www.linkedin.com/in/kartik-bhargav-93a3aa1b0/)")
    st.write("[Saurabh](https://www.linkedin.com/in/saurabh-jejurkar-b80042195)")
    st.write("[Milind](https://www.linkedin.com/in/milind-sai-2017/)")
