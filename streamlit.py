# -------------------------------------- Import Library ------------------------------
import json
## Read Data and Preprocessing Data
import pandas as pd

## Visualization
import plotly.express as px 

## Dashboard 
import streamlit as st 

# ------------------------------ CONFIG ------------------------------
st.set_page_config(
    page_title="Dashboard Analisis Penjualan Properti di NYC",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------- Read dataset ------------------------------
dfm = pd.read_pickle('nyc-rolling-sales.pk')

#----------------------------------Membuat sidebar ----------------------------------
with st.sidebar:
    # Menambahkan logo pribadi
    st.write("Halo, Selamat Datang!")
    st.image("data-science.png")
    st.write("""
             Saya Yohana Poetri Imelda mempersembahkan Dashboard Analisis 
             Penjualan Properti di NYC, sebuah alat yang  menganalisis 
             data perusahaan dengan visualisasi yang interaktif.
             """)
    st.caption('Copyright © Yohana Poetri Imelda 2024')

#--------------------------- ROW 1 -----------------------------------------
st.write("# Dashboard Analisis Penjualan Properti di NYC")
st.write("""
         Analisis ini menggunakan bahasa pemrograman Python dan visualisasi 
         interaktif (Plotly Express) dan data yang digunakan adalah data penjualan 
         properti di New York City yang diambil dari https://www.kaggle.com/datasets/new-york-city/nyc-property-sales
         """)
with st.expander("Click here to see the dataset"):
    st.write("Data Penjualan Properti Di NYC",dfm)

#--------------------------- ROW 2 -----------------------------------------
st.write("### 1. Bagaimana total units di New York City berdasarkan neighborhood?")


# --------------- C. Persiapan Data
trend = dfm.groupby("NEIGHBORHOOD")['TOTAL UNITS'].sum().reset_index()

# --------------- D. Visualisasi
fig_bar=px.bar(trend.sort_values(by="NEIGHBORHOOD", ascending=True),
       x="NEIGHBORHOOD",
       y="TOTAL UNITS",
       title="Total Units Berdasarkan Neighborhood",
       color_discrete_sequence=['Brown'])

st.plotly_chart(fig_bar)

#--------------------------- ROW 3 -----------------------------------------
st.write("### 2. Bagaimana total units yang terjual di New York City berdasarkan sale date?")


trendd = dfm.groupby('SALE DATE')["TOTAL UNITS"].sum().reset_index()

# --------------- D. Visualisasi
fig_line = px.line(trendd,
        x='SALE DATE',
        y="TOTAL UNITS",
        title=f"Total Units Yang Terjual Berdasarkan Sale Date",
        markers=True,
        color_discrete_sequence=['brown'])

st.plotly_chart(fig_line)



