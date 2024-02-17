import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import init

st.set_page_config(page_title="Reyva", page_icon="5️⃣", layout="wide")

init()

st.title("Diagram penyewa sepeda pada tahun 2011-2012 dengan berlandaskan Musim yang terjadi selama satu tahun")
st.caption("Made by: Reyva Noor Fauzan Gunawan (10122089)")

with st.container(border=True, height=175):
    st.subheader("Deskripsi Diagram & Manfaat dari Informasi yang Didapat")
    st.write(
        "Diagram yang saya buat menggambarkan jumlah penyewa sepeda pada setiap musim dan dampaknya terhadap total penyewa permusimnya. Informasi ini memberikan wawasan yang berharga kepada perusahaan tentang pola permintaan selama berbagai musim dalam setahun. Dengan memahami tren ini, perusahaan dapat mengoptimalkan operasi mereka, termasuk pengelolaan inventaris dan jadwal pemeliharaan, untuk mengakomodasi fluktuasi permintaan yang terjadi secara musiman. Selain itu, dengan pemahaman yang lebih baik tentang tren permintaan musiman, perusahaan dapat menyesuaikan strategi pemasaran dan pengembangan penawaran khusus sesuai dengan kebutuhan pelanggan pada saat itu, membantu mereka mengelola sumber daya dan operasi secara lebih efisien dan efektif sepanjang tahun."
    )

# Load dataset
hour_data = pd.read_csv("dataset/day.csv")

# Dataframe yang akan ditampilkan
data = {
    'Musim': ['Spring', 'Summer', 'Fall', 'Winter'],
    'Jumlah_Penyewa': [471348, 918589, 1061129, 841613],
    'Persen': ['14.31%', '27.89%', '32.22%', '25.56%']
}

df = pd.DataFrame(data)

with st.container():
    st.subheader("Tabel Data Penyewa Sepeda")
    st.write(df, type='table', justify='center')

st.write('<hr>', unsafe_allow_html=True)
st.header("Diagram penyewa sepeda pada tahun 2011-2012 berdasarkan musim")


# Data yang telah Anda berikan
musim = ['Spring', 'Summer', 'Fall', 'Winter']
total_setiap_musim = [471348, 918589, 1061129, 841613]
persen_setiap_musim = [(i / sum(total_setiap_musim)) * 100 for i in total_setiap_musim]

# Membuat DataFrame
df_Penyewa_Musim = pd.DataFrame({'Musim': musim, 'Jumlah_Penyewa': total_setiap_musim, 'Persen': persen_setiap_musim})

# Menampilkan diagram batang menggunakan Streamlit
st.bar_chart(df_Penyewa_Musim.set_index('Musim')['Persen'],
             color='#ffad61')

st.expander("**Penjelasan Diagram Batang**", expanded=False).write(
    "Diagram diatas menunjukan bahwa pelanggan lebih banyak menyewa sepeda pada musim gugur/fall dengan total 1 juta lebih, sehingga perusahan dapat memutuskan agar mengatuh pengeluaran untuk biaya pemeliharaan lebih banyak ketika ingin memasuki atau setelah musim gugur"
    )
