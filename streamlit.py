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
    st.write("Halo, selamat datang!")
    st.image("data-science.png")
    st.write("""
             Saya Yohana Poetri Imelda mempersembahkan Dashboard Analisis 
             Penjualan Properti di NYC, sebuah alat yang menganalisis 
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
st.write("### 1. Bagaimana jumlah residential units dan commercial units yang terjual di New York City berdasarkan sale date?")

# ---------- A. Filter Indicator
choices = st.radio("Pick One Indicator!",
         ["RESIDENTIAL UNITS","COMMERCIAL UNITS"])

# ----------- B. Filter Date - Input Rentang Tanggal
min_date = dfm['SALE DATE'].min()
max_date = dfm['SALE DATE'].max()

# Input Date
start_date, end_date = st.date_input("Pick a Date Range!",
              value=[min_date, max_date],
              min_value=min_date,
              max_value=max_date)

# Ubah tipe data input date
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data
cond_min_max = (dfm['SALE DATE'] >= start_date) & (dfm['SALE DATE'] <= end_date)
filtered_dfm = dfm[cond_min_max]

trend = filtered_dfm.groupby("SALE DATE")[choices].sum().reset_index()

# --------------- D. Visualisasi
fig_line = px.line(trend,
        x="SALE DATE",
        y=choices,
        title="JUMLAH {choices} YANG TERJUAL BERDASARKAN SALE DATE",
        markers=True,
        color_discrete_sequence=['blue'])

st.plotly_chart(fig_line)


# --------------- C. Persiapan Data
st.write("### 2. Bagaimana jumlah residential units dan commercial units yang terjual di New York City berdasarkan neighborhood?")
choices = st.radio("Pick One Indicator!",
         ["RESIDENTIAL UNITS","COMMERCIAL UNITS"])
filtered_dfm = dfm[cond_min_max]
trend = filtered_dfm.groupby("NEIGHBORHOOD")[choices].sum().reset_index()

# --------------- D. Visualisasi
fig_bar=px.bar(trend.sort_values(by="NEIGHBORHOOD", ascending=True),
       x="NEIGHBORHOOD",
       y=choices,
       title="JUMLAH {choices} YANG TERJUAL BERDASARKAN NEIGHBORHOOD",
       color_discrete_sequence=['Brown'])

st.plotly_chart(fig_bar)

#--------------------------- ROW 3 -----------------------------------------
st.write("### 3. Bagaimana total units yang terjual di New York City berdasarkan sale date?")


trendd = dfm.groupby('SALE DATE')["TOTAL UNITS"].sum().reset_index()

# --------------- D. Visualisasi
fig_line = px.line(trendd,
        x='SALE DATE',
        y="TOTAL UNITS",
        title=f"TOTAL UNITS YANG TERJUAL BERDASARKAN SALE DATE",
        markers=True,
        color_discrete_sequence=['yellow'])

st.plotly_chart(fig_line)



