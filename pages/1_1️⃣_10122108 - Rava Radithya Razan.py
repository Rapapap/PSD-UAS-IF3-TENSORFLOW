import streamlit as st
import pandas as pd
from utils import init

st.set_page_config(page_title="Rava", page_icon="1️⃣", layout="wide")

init()

# Load dataset
hour_data = pd.read_csv("dataset\hour.csv")

# Membuat Peak Hour Weekday
hour_data["dteday"] = pd.to_datetime(hour_data["dteday"])
hour_data["is_weekend"] = hour_data["weekday"].apply(lambda x: 1 if x in [0, 6] else 0)
peak_hours_weekday = (
    hour_data[hour_data["is_weekend"] == 0].groupby("hr")["cnt"].mean().reset_index()
)
peak_hours_weekend = (
    hour_data[hour_data["is_weekend"] == 1].groupby("hr")["cnt"].mean().reset_index()
)

# Fungsi untuk membuat grafik



st.title("Grafik Pemakaian Rental Sepeda pada Weekday dan Weekend Berdasarkan Jam")

# Menampilkan Dataframe
with st.container():
    st.subheader("Dataframe Weekend")
    st.dataframe(
        peak_hours_weekend,
        column_config={"hr": {"format": "{:.0f}"}, "cnt": {"format": "{:.0f}"}},
        width=500,
        height=300,
    )
    st.subheader("Dataframe Weekday")
    st.dataframe(
        peak_hours_weekday,
        column_config={"hr": {"format": "{:.0f}"}, f"cnt": {"format": "{:.0f}"}},
        width=500,
        height=300,
    )

