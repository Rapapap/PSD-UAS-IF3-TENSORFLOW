import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils import init

st.set_page_config(page_title="Zaidan", page_icon="1️⃣", layout="wide")

init()

st.title("Zaidan Abdul Aziz")
st.subheader('Informasi Diri')
st.text('Nama       : Zaidan Abdul Aziz')
st.text('Nim        : 10122106')
st.text('Kelas      : IF3')
st.write('<hr>', unsafe_allow_html=True)
st.text('Pertanyaan : Apakah pada setiap musim memengaruhi penjumlahan penyewa sepeda?')
st.write(pd.read_csv('day.csv'))