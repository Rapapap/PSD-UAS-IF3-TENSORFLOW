import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import init

st.set_page_config(page_title="Zaidan", page_icon="1️⃣", layout="wide")

init()

st.title('Informasi Diri')
st.text('Nama       : Zaidan Abdul Aziz')
st.text('Nim        : 10122106')
st.text('Kelas      : IF3')
st.write('<hr>', unsafe_allow_html=True)
st.text('Pertanyaan : Apakah pada setiap musim memengaruhi penjumlahan penyewa sepeda?')

st.write("Menyiapkan data-data yang akan dipakai untuk proses analisis data. Dalam proyek data ini data yang akan dipakai adalah 'Bike Sharing Dataset', lebih tepatnya 'day.csv' dan 'hour.csv'")
day_data = pd.read_csv('https://raw.githubusercontent.com/Rapapap/PSD-UAS-IF3-TENSORFLOW/tree/zaidan/dataset/day.csv')
st.write("day.csv",day_data)

# Mendapatkan Seluruh penyewa pada masing-masing musim
Jumlah_cnt_s1 = day_data.query("season == 1")['cnt'].sum()
Jumlah_cnt_s2 = day_data.query("season == 2")['cnt'].sum()
Jumlah_cnt_s3 = day_data.query("season == 3")['cnt'].sum()
Jumlah_cnt_s4 = day_data.query("season == 4")['cnt'].sum()

musim = ['Spring','Summer','Fall','Winter']
total_setiap_musim = [Jumlah_cnt_s1,Jumlah_cnt_s2,Jumlah_cnt_s3,Jumlah_cnt_s4]

total = sum(total_setiap_musim)
persen_setiap_musim = []
for i in total_setiap_musim:
  persen_setiap_musim.append((i/total)*100)

df_Penyewa_Musim = pd.DataFrame({'Musim' : musim, 'Jumlah_Penyewa' : total_setiap_musim, 'Persen' : persen_setiap_musim})
df_Penyewa_Musim_1 = pd.DataFrame({'Musim' : musim, 'Jumlah_Penyewa' : total_setiap_musim})

st.write("Jumlah Penyewa pada tahun 2011-2012")
st.write(df_Penyewa_Musim)
st.write("Dengan tipe data berikut")
st.write(df_Penyewa_Musim.dtypes)

warna = ['#736ff8','#736ff8','#201dac','#736ff8']

fig, ax = plt.subplots()
ax.bar(
    df_Penyewa_Musim['Musim'], 
    df_Penyewa_Musim['Persen'], 
    color=warna
)

for i, p in enumerate(df_Penyewa_Musim['Persen']):
  ax.text(i, p, f'{p:.2f}%', ha='center', va='bottom')

ax.set_xlabel('Musim')
ax.set_ylabel('Total Penyewa dalam Persen')
ax.set_title('Data Penyewa Sepeda tahun 2011-2012')
st.pyplot(fig)

with st.expander("Penjelasan musim memengaruhi penjumlahan penyewa sepeda"):
    st.write("- Berdasarkan jumlah penyewa pada data, dapat disimpulkan bahwa pada setiap musim memengaruhi penjumlahan penyewa.\n- Diperlihatkan bahwa orang-orang menyukai menyewa sepeda pada Musim Gugur (Fall).\n- Musim Semi (Spring) merupakan penyewa paling sedikit dibandingkan dengan musim yang lainnya.")