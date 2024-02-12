# Panduan push code ke github
1. Pindah ke branch yang sudah disediakan sesuai dengan nama kalian, dengan list branch sebagai berikut:<br>
> main, rava, apriana, rizky, ninandya, reyva, zaidan

```bash
# sesuaikan dengan nama kalian, disini contoh akan masuk ke branch rava
git checkout rava
```
2. Lakukan pull code terlebih dahulu saat ingin memulai sesuatu
```bash
git pull origin main
```
3. Silahkan melakukan perubahan code apapun
4. Jika sudah menyelesaikan perubahan code dan akan melakukan push ke repository github, maka lakukan
```bash
git add .
```
5. Lakukan commit untuk memberi tahu pesan perubahannya
```bash
git commit -m "tulis pesan disini"
```
6. Lakukan perintah push ke repository github
```bash
# sesuaikan dengan nama kalian, disini contoh akan push code ke branch rava
git push origin rava
```