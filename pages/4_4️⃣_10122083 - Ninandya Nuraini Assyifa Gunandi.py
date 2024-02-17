import streamlit as st
from utils import init

st.set_page_config(page_title="Nina", page_icon="4️⃣", layout="wide")

init()

st.title('Informasi Diri')
st.text('Nama       : Ninandya Nuraini Assyifa Gunandi)
st.text('Nim        : 10122083')
st.text('Kelas      : IF3')
st.write('<hr>', unsafe_allow_html=True)
st.text('Pertanyaan : Berapa perbandingan anggota casual dan anggota registered pada tahun 2011??')

st.write("Menyiapkan data-data yang akan dipakai untuk proses analisis data. Dalam proyek data ini data yang akan dipakai adalah 'Bike Sharing Dataset', lebih tepatnya ")
day_data = pd.read_csv('dataset\day.csv')
st.write("day.csv",day_data)
