import streamlit as st
import pandas as pd
from utils import init

st.set_page_config(page_title="Rava", page_icon="1️⃣", layout="wide")

init()

# Load dataset
df = pd.read_csv("/dataset/hour.csv")

# Membuat Peak Hour Weekday dan Weekend
hour_data['is_weekend'] = hour_data['weekday'].apply(lambda x: 1 if x in [0, 6] else 0)
peak_hours_weekday = hour_data[hour_data['is_weekend'] == 0].groupby('hr')['cnt'].mean().reset_index()
peak_hours_weekend = hour_data[hour_data['is_weekend'] == 1].groupby('hr')['cnt'].mean().reset_index()

st.title("Grafik Pemakaian Rental Sepeda pada Weekday dan Weekend Berdasarkan Jam")
st.dataframe(peak_hours_weekday)