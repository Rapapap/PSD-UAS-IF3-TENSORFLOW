import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from utils import init

st.set_page_config(page_title="Rizky", page_icon="3️⃣", layout="wide")

init()
st.title("Rizky Aditya Friatna")
st.subheader('Informasi Diri')
st.text('Nama       : Rizky Aditya Friatna')
st.text('Nim        : 10122111')
st.text('Kelas      : IF3')
st.write('<hr>', unsafe_allow_html=True)
st.text('Pertanyaan : Bagaimana bentuk trend rental sepeda pada Tahun 2011?')

with st.container(border=True, height=175):
    st.subheader("Deskripsi Grafik & Manfaat dari Informasi yang Didapat")
    st.write(
        "Grafik di dibawah ini menunjukkan tren jumlah penyewaan sepeda harian pada tahun 2011. Grafik ini menggunakan sumbu x untuk menampilkan tanggal dan sumbu y untuk menampilkan jumlah penyewaan. Setiap titik pada grafik mewakili jumlah penyewaan sepeda harian pada tanggal tertentu. Garis yang menghubungkan titik-titik tersebut menunjukkan bagaimana jumlah penyewaan berubah dari waktu ke waktu. Grafik juga dilengkapi dengan label sumbu, judul grafik, dan legenda yang menjelaskan garis yang ditampilkan.Mamfaatnya seperti mengidentifikasi pola Misalnya, jika terdapat tren peningkatan jumlah penyewaan sepeda, hal ini dapat menjadi indikasi bahwa aktivitas bersepeda semakin populer pada tahun 2011. dan Pemantauan Kinerja misalnya Pemantauan ini dapat membantu dalam mengevaluasi strategi pemasaran"
    )


# Load dataset
day_data = pd.read_csv("dataset/day.csv")
hour_data = pd.read_csv("dataset/hour.csv")

# Ubah kolom 'dteday' menjadi format datetime
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Filter data untuk tahun 2011
day_data_2011 = day_data[day_data['dteday'].dt.year == 2011]
hour_data_2011 = hour_data[hour_data['dteday'].dt.year == 2011]

with st.container():
    # Visualisasi Tren Rental Sepeda Harian
    st.write('## Tren Rental Sepeda Harian Tahun 2011')
    st.line_chart(day_data_2011.set_index('dteday')['cnt'])

with st.container():
    # Visualisasi Tren Rental Sepeda Per Jam Tahun 2011
    # Data per jam (ambil contoh jam 12:00 setiap harinya)
    st.write('## Tren Rental Sepeda perjam Tahun 2011')
    st.line_chart(hour_data_2011[['dteday', 'cnt']][::24].set_index('dteday'), use_container_width=True)





