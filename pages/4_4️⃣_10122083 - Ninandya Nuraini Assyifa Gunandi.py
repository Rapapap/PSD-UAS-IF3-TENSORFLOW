
st.set_page_config(page_title="Nina", page_icon="4️⃣", layout="wide")

init()

st.title('Informasi Diri')
st.text('Nama       : Ninandya Nuraini Assyifa Gunandi)
st.text('Nim        : 10122083')
st.text('Kelas      : IF3')
st.write('<hr>', unsafe_allow_html=True)
st.text('Pertanyaan : Berapa perbandingan anggota casual dan anggota registered pada tahun 2011??')

st.write("Menyiapkan data-data yang akan dipakai untuk proses analisis data. Dalam proyek data ini data yang akan dipakai adalah 'Bike Sharing Dataset')

data = pd.read_csv('/content/drive/MyDrive/day.csv')
data['dteday'] = pd.to_datetime(data['dteday'])

data['year'] = data['dteday'].dt.year

data_2011 = data[data['year'] == 2011]

jumlah_registered_2011 = data_2011['registered'].sum()
jumlah_casual_2011 = data_2011['casual'].sum()

st.text("Jumlah anggota registered pada tahun 2011:", jumlah_registered_2011)
st.text("Jumlah anggota casual pada tahun 2011:", jumlah_casual_2011)

perbandingan = jumlah_registered_2011 - jumlah_casual_2011
print("Perbandingan anggota registered dan casual pada tahun 2011 :", perbandingan)

Type = ['Registered', 'casual']
jumlah =[jumlah_registered_2011,jumlah_casual_2011]

df_registered_casual = pd.DataFrame({'Type' : Type, 'Total' : jumlah})

st.text("Data anggota registered dan casual pada tahun 2011")
display(df_registered_casual)
display(df_registered_casual.dtypes)


fig, ax = plt.subplots()
ax.pie(
    df_registered_casual['Total'],
    labels=df_registered_casual['Type'],
    autopct='%1.1f%%',
    startangle=90,
    colors=['#84c6da', '#50c3c9'],
    wedgeprops={"linewidth": 1.5, "edgecolor": "white"}
    )
    
ax.title('Perbandingan Anggota Registered dan Anggota Casual\n(Tahun 2011)')
ax.show()

