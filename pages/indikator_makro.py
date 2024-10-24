import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import lxml


st.caption("Terdiri dari 3 kelurahan")
#membaca file excel
opendata = pd.read_excel("data/kelompokumur.xlsx")
st.dataframe(opendata, use_container_width=True, hide_index=True)

#membuat grafik batang
fig = px.bar(opendata, x="Jumlah", y="Kelompok Umur")
st.plotly_chart(fig)