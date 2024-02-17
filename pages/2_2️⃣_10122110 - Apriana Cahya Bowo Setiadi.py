import streamlit as st
import pandas as pd
from utils import init
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Apriana", page_icon="2️⃣", layout="wide")

init()

st.title("Hello, Welcome to Apriana Page :sunglasses:")
st.text('Nama       : Apriana Cahya Bowo Setiadi')
st.text('Nim        : 10122110')
# garis pembatas
st.markdown('---')

# Load data
day_data = pd.read_csv('dataset/day.csv')
hour_data = pd.read_csv('dataset/hour.csv')

# Rename column cnt 
day_data = day_data.rename(columns={'cnt':'total'})
hour_data = hour_data.rename(columns={'cnt':'total'})

def create_count_rental(df):
    daily_rent = df.groupby(by='dteday').agg({'total': 'sum'}).reset_index()
    daily_casual_rent = df.groupby(by='dteday').agg({'casual': 'sum'}).reset_index()
    daily_registered_rent = df.groupby(by='dteday').agg({'registered': 'sum'}).reset_index()
    return daily_rent, daily_casual_rent, daily_registered_rent

def create_day_temp_total(df):
    day_temp = df['temp']
    day_total = df['total']
    day_temp_celcius = day_temp * 41
    day_temp_total = pd.concat([day_temp_celcius,day_total], axis=1)
    return day_temp_total

def create_day_weathersit_total(df):
    day_weathersit = df['weathersit']
    day_total = df['total']
    day_weathersit_total = pd.concat([day_weathersit,day_total], axis=1)
    day_weathersit_total['weathersit'] = day_weathersit_total['weathersit'].replace([1,2,3,4],['Clear','Mist','Light Snow','Heavy Rain'])
    day_weathersit_total = day_weathersit_total.groupby('weathersit').sum()
    return day_weathersit_total

def plot_day_temp_total(df):
    fig = px.scatter(day_temp_total, x='temp', y='total', title='Penyebaran Data Jumlah Peminjam Sepeda dan Temperature Cuaca', labels={'temp':'Temperature', 'total':'Jumlah'})
    st.plotly_chart(fig)

def plot_day_weathersit_total(df):
    fig = px.bar(day_weathersit_total, x=day_weathersit_total.index, y='total', title='Total Peminjam Sepeda Berdasarkan Cuaca', labels={'index':'Weather Situation', 'total':'Jumlah'})
    st.plotly_chart(fig)
    
# 1
st.subheader('Total Rentals')
st.markdown('''
    Dengan mengetahui total peminjam berdasarkan rentang waktu tertentu, kita bisa mengetahui jumlah peminjam sepeda yang terjadi pada rentang waktu tersebut. dengan itu bisa menjadi bahan evaluasi bagi penyewa ketika jumlah peminjaman turun di rentang waktu tertentu maka harus di cek setiap faktornya yang mempengaruhi jumlah peminjaman sepeda tersebut. bisa dari cuaca, temperature, hari libur, dan lainnya
''')
min_date = pd.to_datetime(day_data['dteday']).dt.date.min()
max_date = pd.to_datetime(day_data['dteday']).dt.date.max()

start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value= min_date,
        max_value= max_date,
        value=[min_date, max_date]
    )
total_rental_range = day_data[(day_data['dteday'] >= str(start_date)) & 
                (day_data['dteday'] <= str(end_date))]

col1, col2, col3 = st.columns(3)
daily_rent, daily_casual_rent, daily_registered_rent = create_count_rental(total_rental_range)

with col1:
    daily_rent_casual = daily_casual_rent['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)

with col3:
    daily_rent_total = daily_rent['total'].sum()
    st.metric('Total User', value= daily_rent_total)

# 2
st.header("Grafik Penyebaran Data Jumlah Peminjam Sepeda dan Temperature Cuaca")
st.markdown('''
    Dengan mengetahui penyebaran data jumlah peminjam sepeda dan temperature cuaca, kita bisa mengetahui bahwa peminjaman sepeda dipengaruhi oleh temperature cuaca karena :blue[orang lebih memilih untuk bersepeda di suhu lingkungan yang enak, seperti suhu 20-30 derajat celcius.] Hal ini bisa menjadi persiapan bagi penyewa ketika suhu cuaca sedang normal maka harus dilakukan pengecekan semua sepeda agar bisa di sewakan sesuai dengan permintaan 
''')
day_temp_total = create_day_temp_total(day_data)
st.dataframe(day_temp_total.head())
plot_day_temp_total(day_temp_total)
st.expander("**Penjelasan Grafik**", expanded=False).write(
    "Grafik di atas menunjukkan penyebaran data jumlah peminjam sepeda dan temperature cuaca. Dari grafik tersebut, kita dapat melihat bahwa peminjaman sepeda cenderung tinggi pada suhu 20-30 derajat celcius. Hal ini menunjukkan bahwa faktor yang mempengaruhi total peminjaman sepeda salah satunya yaitu temperature cuaca."
)

# 3
st.header("Grafik Total Peminjam Sepeda Berdasarkan Cuaca")
st.markdown('''
    Dengan melihat grafik total peminjaman sepeda berdasarkan cuaca, kita bisa melihat bahwa pada cuaca yang cerah, :blue[jumlah peminjam sepeda lebih banyak dibandingkan dengan cuaca yang lain.] Hal ini bisa menjadi pertimbangan bagi penyewa ketika cuaca sedang cerah maka harus dilakukan pengecekan semua sepeda agar bisa di sewakan sesuai dengan permintaan 
''')
day_weathersit_total = create_day_weathersit_total(day_data)
st.dataframe(day_weathersit_total)
plot_day_weathersit_total(day_weathersit_total)
st.expander("**Penjelasan Grafik**", expanded=False).write(
    "Grafik di atas menunjukkan bahwa peminjaman sepeda pada cuaca yang clear atau cerah memiliki jumlah peminjam sepeda yang lebih banyak dibandingkan dengan cuaca yang lain yaitu sebanyak 2.257.952 orang. Hal ini menunjukkan bahwa cuaca yang cerah memiliki pengaruh yang signifikan terhadap jumlah peminjam sepeda."
)