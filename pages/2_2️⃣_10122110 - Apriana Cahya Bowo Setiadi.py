import streamlit as st
import pandas as pd
from utils import init
import matplotlib.pyplot as plt

st.set_page_config(page_title="Apriana", page_icon="2️⃣", layout="wide")

init()

st.title("Hello, Welcome to Apriana Page :sunglasses:")
st.subheader('Informasi Diri')
st.text('Nama       : Apriana Cahya Bowo Setiadi')
st.text('Nim        : 10122110')
# garis pembatas
st.markdown('---')

# Load data
day_data = pd.read_csv('dataset/day.csv')
hour_data = pd.read_csv('dataset/hour.csv')

# Rename column cnt 
day_data = day_data.rename(columns={'cnt':'total'})

# Menampilkan data
st.dataframe(day_data.head())
st.dataframe(hour_data.head())

day_temp = day_data['temp']
day_total = day_data['total']
day_temp_celcius = day_temp * 41
day_temp_total = pd.concat([day_temp_celcius,day_total], axis=1)

fig, ax = plt.subplots()
plt.scatter(day_temp_total['temp'],day_temp_total['total'])
plt.xlabel('Temperature')
plt.ylabel('Jumlah')
plt.title('Penyebaran Data Jumlah Peminjam Sepeda dan Temperature Cuaca')
# rezie the figure
fig.set_size_inches(10,5)

st.header("Grafik Penyebaran Data Jumlah Peminjam Sepeda dan Temperature Cuaca")
st.markdown('''
  Dengan mengetahui penyebaran data jumlah peminjam sepeda dan temperatur cuaca, kita bisa mengetahui bahwa peminjaman sepeda dipengaruhi oleh temperature cuaca karena orang lebih memilih untuk bersepeda di suhu lingkungan yang enak, seperti suhu 20-30 derajat celcius. Hal ini bisa menjadi persiapan bagi penyewa ketika suhu cuaca sedang normal maka harus dilakukan pengecekan semua sepeda agar bisa di sewakan sesuai dengan permintaan 
''')
st.dataframe(day_temp_total.head())
st.pyplot(fig)


# 2
