# PSD-UAS-IF1-FOLIUM
>Untuk mengakses dashboard secara online, klik link dibawah ini <br>
<a href="https://psd-uas-if1-folium.streamlit.app/" style="font-size: 1.5rem;">Web Streamlit Online</a>

## Setup Environment:
> Ini penting agar setiap orang menjalankan program dengan versi _dependencies_ yang sama.

1. Cek versi Python terlebih dahulu. Pastikan versi python yang digunakan merupakan v3.9. Jika bukan v3.9 dapat download [disini](https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe).
```bash
python --version
```
2. Buatlah environment python v3.9 dengan cara masuk ke terminal, lalu ketik
```bash
python3.9 -m venv env
```
3. Aktifkan environment python yang baru saja dibuat
```bash
.\env\Scripts\activate
```
4. Install _dependencies_
```bash
pip install -r requirements.txt
```

## Cara menjalankan program secara local
1. Setiap mulai, pastikan env sudah aktif
```bash
.\env\Scripts\activate
```
2. Jalankan program Streamlit
```bash
streamlit run 📊_Dashboard.py
```
3. Jika sudah selesai dan akan keluar dari program, pastikan environment sudah di nonaktifkan, dengan cara
```bash
deactivate
```