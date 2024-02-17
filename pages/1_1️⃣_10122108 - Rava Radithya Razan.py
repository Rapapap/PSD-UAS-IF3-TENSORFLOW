import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from utils import init

st.set_page_config(page_title="Rava", page_icon="1️⃣", layout="wide")

init()

# Load dataset
hour_data = pd.read_csv("dataset/hour.csv")

# Membuat Peak Hour Weekday
hour_data["dteday"] = pd.to_datetime(hour_data["dteday"])
hour_data["is_weekend"] = hour_data["weekday"].apply(lambda x: 1 if x in [0, 6] else 0)
peak_hours_weekday = (
    hour_data[hour_data["is_weekend"] == 0].groupby("hr")["cnt"].mean().reset_index()
)
peak_hours_weekend = (
    hour_data[hour_data["is_weekend"] == 1].groupby("hr")["cnt"].mean().reset_index()
)


# Fungsi untuk membuat grafik
def plot_peak_hours_plotly(peak_hours_weekday, peak_hours_weekend):
    fig = px.line(
        peak_hours_weekday,
        x="hr",
        y="cnt",
        title="Average Bike Rentals per Hour",
        labels={"hr": "Hour of the Day", "cnt": "Average Rentals"},
    )
    fig.add_scatter(
        x=peak_hours_weekend["hr"],
        y=peak_hours_weekend["cnt"],
        mode="lines",
        name="Weekend",
    )
    fig.add_scatter(
        x=peak_hours_weekday["hr"],
        y=peak_hours_weekday["cnt"],
        mode="lines",
        name="Weekday",
    )
    fig.update_xaxes(
        tickmode="linear", tick0=0, dtick=1
    )  # Display each step of the x-axis
    st.plotly_chart(fig, use_container_width=True, theme=None)


st.title(
    ":orange[Grafik Pemakaian Rental Sepeda pada Weekday dan Weekend Berdasarkan Jam]"
)

with st.container(border=True, height=175):
    st.subheader(":orange[Deskripsi Grafik & Manfaat dari Informasi yang Didapat]")
    st.write(
        "Grafik ini menunjukkan rata-rata peminjaman sepeda per jam pada hari kerja dan akhir pekan. Informasi yang didapatkan dari grafik ini dapat memberikan pemahaman tentang pola penggunaan sepeda pada jam-jam tertentu pada hari kerja dan akhir pekan. Hal ini dapat membantu dalam perencanaan dan pengelolaan sumber daya sepeda, seperti menentukan waktu-waktu dengan permintaan tinggi dan rendah, serta mengoptimalkan penempatan sepeda di berbagai lokasi."
    )

# Menampilkan Dataframe
st.subheader("Dataframe Weekend")
col1, col2 = st.columns([1, 1.8])

st.subheader("Dataframe Weekday")
col3, col4 = st.columns([1, 1.8])

with col1:
    st.dataframe(
        peak_hours_weekend.rename(columns={"hr": "Hour", "cnt": "Average Rentals"}),
        column_config={"hr": {"format": "{:.0f}"}, "cnt": {"format": "{:.0f}"}},
        width=500,
        height=300,
    )
with col2:
    st.write(
        '''
        Dataframe ini menampilkan rata-rata aktifitas rental sepeda pada weekend. Berikut penjelasan kolom dataframe:
        
        - hr: Jam dalam sehari
        - count: Jumlah rata-rata rental sepeda pada jam tersebut'''
    )

with col3:
    st.dataframe(
        peak_hours_weekday.rename(columns={"hr": "Hour", "cnt": "Average Rentals"}),
        column_config={"hr": {"format": "{:.0f}"}, f"cnt": {"format": "{:.0f}"}},
        width=500,
        height=300,
    )
with col4:
    st.write(
        '''
        Dataframe ini menampilkan rata-rata aktifitas rental sepeda pada weekend. Berikut penjelasan kolom dataframe:
        
        - hour: Jam dalam sehari
        - count: Jumlah rata-rata rental sepeda pada jam tersebut'''
    )

# Menampilkan Grafik
plot_peak_hours_plotly(peak_hours_weekday, peak_hours_weekend)
st.expander("**:orange[penjelasan Grafik]**", expanded=False).write(
    "Grafik di atas menunjukkan rata-rata peminjaman sepeda per jam pada hari kerja dan akhir pekan. Dari grafik tersebut, kita dapat melihat bahwa peminjaman sepeda pada hari kerja memiliki dua puncak, yaitu pada jam 8 pagi dan jam 5 sore. Sedangkan pada akhir pekan, peminjaman sepeda cenderung stabil sepanjang hari, dengan puncak pada jam 1 siang. Grafik ini dapat memberikan informasi yang berguna dalam perencanaan dan pengelolaan sumber daya sepeda."
)   
st.caption("Made by: 10122108 Rava Radithya Razan")

