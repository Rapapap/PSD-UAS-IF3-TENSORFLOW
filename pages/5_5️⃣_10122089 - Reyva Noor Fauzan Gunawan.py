import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils import init

st.set_page_config(page_title="Reyva", page_icon="5️⃣", layout="wide")

init()

st.title("Reyva Noor Fauzan Gunawan")
st.header("Informasi Diri Saya")
st.write("Nama  : Reyva Noor Fauzan Gunawan")
st.write("NIM   : 10122089")
st.write("Kelas : IF-3")
st.write('<hr>', unsafe_allow_html=True)
st.title("Pertanyaan:")
    st.write("Pada musim apa sepeda sering disewakan ketika hujan oleh para penyewa?")
    st.write("Bagaimana data ini akan membantu untuk mengelola pemeliharaan sepeda?")

if __name__ == "__main__":
    main()
