# MATH EXERCISE
# melatih pengetahuan dasar module math

import math

# Kalkulator luas lingkaran
jari_jari = float(input("Masukan jari-jari lingkarang : "))

luas_lingkarang = round(math.pi,2) * pow(jari_jari, 2)
print(f"Luas lingkarang sebesar = {luas_lingkarang} cm^2")
print()


# Teorema pythagoras
a = 3
b = 4
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(c)
print()

# Kasus penggunaan math.floor()
# KASUS 1: Sistem Diskon Bertingkat
# Cerita:
# Toko online punya sistem diskon:

# Belanja Rp 100.000 = dapat 1 voucher
# Belanja Rp 250.000 = dapat 2 voucher
# Belanja Rp 350.000 = dapat 3 voucher
# Aturan: Setiap kelipatan Rp 100.000 dapat 1 voucher (dibulatkan ke bawah)

belanja = float(input("Kamu belanja berapa ( mendapatkan 1 voucher minimal belanja 100.000 ) : "))
voucher = belanja / 100000
print(f"Voucher yang ada dapat adalah = {math.floor(voucher)}")


# Kasus penggunaan math.ceil()
# KASUS 2: Pemesanan Bus Wisata
# Cerita:
# Rombongan sekolah mau study tour. 1 bus muat 45 orang. Kalau kurang dari 45, tetap harus sewa 1 bus.

siswa = float(input("Jumlah siswa ( 45 siswa untuk 1 bus, jika lebih sewa 1 bus lagi ) : "))
bus = math.ceil(siswa/45)
print(f"Bus yang harus di sewa adalah = {bus}")
