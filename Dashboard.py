import streamlit as st
import pandas as pd
from utils import init

st.set_page_config(
    page_title="Dashboard IF-3 Kelompok Tensorflow", page_icon="🚲", layout="wide"
)

init()

# Load dataset
hour_df = pd.read_csv("dataset/hour.csv")
day_df = pd.read_csv("dataset/day.csv")


# Fungsi untuk menampilkan dataset
def show_dataset_hour():
    st.header("Dataset")
    st.write(
        """Dataset ini berisi data peminjaman sepeda per jam yang mencakup informasi cuaca dan musim. Data ini diambil dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)."""
    )
    st.write("Berikut adalah 5 baris pertama dari dataset ini:")
    st.write(hour_df.head())


def show_dataset_day():
    st.header("Dataset")
    st.write(
        """Dataset ini berisi data peminjaman sepeda per hari yang mencakup informasi cuaca dan musim. Data ini diambil dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)."""
    )
    st.write("Berikut adalah 5 baris pertama dari dataset ini:")
    st.write(day_df.head())


# Fungsi untuk menampilkan penjelasan dataset
def show_hour_dataset_description():
    st.write(
        """Dataset ini berisi data peminjaman sepeda per jam yang mencakup informasi cuaca dan musim. Data ini diambil dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)."""
    )
    st.write("""Berikut adalah penjelasan dari setiap kolom pada dataset ini:""")
    st.write("""
    - instant: ID dari setiap baris data
    - dteday: Tanggal peminjaman sepeda
    - season: Musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin)
    - yr: Tahun (0: 2011, 1: 2012)
    - mnth: Bulan (1 - 12)
    - hr: Jam (0 - 23)
    - holiday: Apakah hari libur atau bukan (1: ya, 0: tidak)
    - weekday: Hari dalam seminggu (0 - 6)
    - workingday: Apakah hari kerja atau bukan (1: ya, 0: tidak)
    - weathersit: Kondisi cuaca (1: cerah, 2: berkabut, 3: hujan ringan/hujan salju ringan, 4: hujan lebat/hujan salju lebat)
    - temp: Suhu dalam derajat Celsius
    - atemp: Suhu yang dirasakan dalam derajat Celsius
    - hum: Kelembaban relatif
    - windspeed: Kecepatan angin
    - casual: Jumlah peminjaman sepeda oleh pengguna non-terdaftar
    - registered: Jumlah peminjaman sepeda oleh pengguna terdaftar
    - cnt: Jumlah total peminjaman sepeda (casual + registered)"""
    )


def show_day_dataset_description():
    st.write(
        """Dataset ini berisi data peminjaman sepeda per hari yang mencakup informasi cuaca dan musim. Data ini diambil dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)."""
    )
    st.write("""Berikut adalah penjelasan dari setiap kolom pada dataset ini:""")
    st.write("""
    - instant: ID dari setiap baris data
    - dteday: Tanggal peminjaman sepeda
    - season: Musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin)
    - yr: Tahun (0: 2011, 1: 2012)
    - mnth: Bulan (1 - 12)
    - holiday: Apakah hari libur atau bukan (1: ya, 0: tidak)
    - weekday: Hari dalam seminggu (0 - 6)
    - workingday: Apakah hari kerja atau bukan (1: ya, 0: tidak)
    - weathersit: Kondisi cuaca (1: cerah, 2: berkabut, 3: hujan ringan/hujan salju ringan, 4: hujan lebat/hujan salju lebat)
    - temp: Suhu dalam derajat Celsius
    - atemp: Suhu yang dirasakan dalam derajat Celsius
    - hum: Kelembaban relatif
    - windspeed: Kecepatan angin
    - casual: Jumlah peminjaman sepeda oleh pengguna non-terdaftar
    - registered: Jumlah peminjaman sepeda oleh pengguna terdaftar
    - cnt: Jumlah total peminjaman sepeda (casual + registered)"""
    )


# UI
st.title(":orange[Bike Sharing Dataset Dashboard]")
st.write(
    """Selamat datang di dashboard kami! Dashboard ini dibuat untuk memvisualisasikan data dari dataset Bike Sharing.
         Dataset ini berisi data peminjaman sepeda per jam yang mencakup informasi cuaca dan musim."""
)
st.write("Silakan pilih dataset yang ingin Anda lihat:")
dataset = st.radio("", ("Dataset Per Jam", "Dataset Per Hari"))

if dataset == "Dataset Per Jam":
    show_dataset_hour()
    show_hour_dataset_description()
else:
    show_dataset_day()
    show_day_dataset_description()
