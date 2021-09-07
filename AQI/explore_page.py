import streamlit as st
import streamlit.components as stc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import ExtraTreesRegressor
import matplotlib
import plotly_express as px
import base64


# config changes
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)


def show_explore_page():
    # title
    st.title("Data Exploration")
    st.sidebar.subheader("Visualization Settings")

    def load_data():
        df = pd.read_csv("final_data.csv")
        return df

    df = load_data()

    def get_table_download_link_csv(df):
        csv = df.to_csv().encode()
        b64 = base64.b64encode(csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="sample.csv" target="_blank">Download dataset</a>'
        return href

    st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)

    st.write(df)

    st.write('(Rows,Columns) =', df.shape)

    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)


# adding select widget to sidebar - chart select
    chart_select = st.sidebar.selectbox(
        label="Select the chart type",
        options=["Scatterplot", "Boxplot", "Histograms",
                 "Density Contour", "Density Heatmap"])
    if chart_select == "Scatterplot":
        st.sidebar.subheader("Scatterplot options")
        try:
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            plot = px.scatter(data_frame=df, x=x_values, y=y_values)
            # displaying the chart
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == "Boxplot":
        st.sidebar.subheader("Boxplot options")
        try:
            x_values = st.sidebar.selectbox("Feature", options=numeric_columns)
            bxplot = px.box(df[x_values])
            # displaying the chart
            st.plotly_chart(bxplot)
        except Exception as e:
            print(e)

    if chart_select == "Histograms":
        st.sidebar.subheader("Histogram options")
        try:
            x_values = st.sidebar.selectbox("Feature", options=numeric_columns)
            bins = st.sidebar.slider("No. of bins", 0, 100, 50)
            histplot = px.histogram(df[x_values], nbins=bins)
            # displaying the chart
            st.plotly_chart(histplot)
        except Exception as e:
            print(e)

    if chart_select == "Density Contour":
        st.sidebar.subheader("Density Contour options")
        try:
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            dencplot = px.density_contour(data_frame=df,
                                          x=x_values, y=y_values)
            # displaying the chart
            st.plotly_chart(dencplot)
        except Exception as e:
            print(e)

    if chart_select == "Density Heatmap":
        st.sidebar.subheader("Density Heatmap options")
        try:
            x_values = st.sidebar.selectbox("X axis", options=numeric_columns)
            y_values = st.sidebar.selectbox("Y axis", options=numeric_columns)
            denhplot = px.density_heatmap(data_frame=df, x=x_values, y=y_values,
                                          marginal_x="box", marginal_y="violin")
            # displaying the chart
            st.plotly_chart(denhplot)
        except Exception as e:
            print(e)
