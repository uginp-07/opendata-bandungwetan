import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import lxml

st.title("Streamlit Open Data Bandung Wetan")
st.header("Kelurahan", divider="rainbow")
st.caption("Terdiri dari 3 kelurahan")
st.subheader("Tamansari", divider="green")
st.write("RT RW")
st.caption("caption")

st.subheader("" , divider="blue")

kolom1, kolom2, kolom3 = st.columns(3)
with kolom1: 
    st.header("Kelurahan", divider="rainbow")
with kolom2: 
    st.subheader("Tamansari", divider="green")
with kolom3:
    st.caption("Terdiri dari 3 kelurahan")

st.subheader("", divider="green")

kolom4, kolom5, kolom6 = st.columns(3)
with kolom4: 
    with st.container(border=True):
        st.header("Kelurahan", divider="rainbow")
with kolom5: 
    with st.container(border=True):
        st.subheader("Tamansari", divider="green")
with kolom6:
    with st.container(border=True):
        st.caption("Terdiri dari 3 kelurahan")

#membaca file excel
opendata = pd.read_excel("data/kelompokumur.xlsx")
st.dataframe(opendata, use_container_width=True, hide_index=True)

#membuat grafik batang
fig = px.bar(opendata, x="Kelompok Umur", y="Jumlah")
st.plotly_chart(fig)

#membuat grafik batang
fig1 = px.line(opendata, x="Kelompok Umur", y="Jumlah")
st.plotly_chart(fig1)

