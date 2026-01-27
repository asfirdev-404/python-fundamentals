# MATH
# berfungsi untuk mempermudah porses yang berhubungan dengan perhitungan

# Bawaan dari python / Built-in : 

# round()
# berfungsi untuk membulatkan bilangan angka

print(round(-3.14)) # akan di bulatkan
print(round(0.5)) # jika angka desimal > .5 maka akan di bulan kan kedepan, di kasus ini tidak jadi 0 tapi menjadi 1

print(round(1.234567, 2)) # akan mengeluarkan bilangan decimal yang hanya memperlihatkan 2 angka saja di belakang titik
print(round(1.234567, 3)) # akan mengeluarkan bilangan decimal yang hanya memperlihatkan 3 angka saja di belakang titik
print(round(1299.32, -2)) # akan membulatkan bilangan decimal dan bilangat bulat nya atau membuat bilangan bulat nya di di bulatkan juga sebanyak 2 bilangan belakang nya 
print()

# pow()
# berfungsi untuk perpangkatan bilangan angka 

print(pow(5, 2)) # angka pertama akan di pangkatkan dengan angka kedua
print(pow(5, 3)) # pow(a, b) == a ** b

print(pow(5, 3, 4)) # jarang di pakai namun ini sama fungsi nya seperti ini, pow(a, b, c) == a ** b % c
print()


# abs()
# berfungsi untuk mengubah bilangan menjadi nilai mutlak atau mengubah nilai nya dari yang negatif menjadi positif dan yang positif tetap positif

print(abs(10)) # tetap
print(abs(-113)) # di ubah menjadi positif
print(abs(10.5)) # tetap
print(abs(-3.14)) # di ubah menjadi positif

print(abs(5 - 125)) # ini untuk menghitung selisih angka
print(abs(125 - 5)) # ini untuk menghitung selisih angka
print()


# max()
# berfungsi untuk mencari angka terbesar dari sekumpulan angka
print(max(4,4,2,4,5,7,1,13,23,5,90,0,2)) # bisa mencari angka terbesar secara manual
a = [1,3,5,2,4,7,1,5,6,9]
print(max(a)) # bisa mencari angka terbesar dalam list
print()


# min()
# sama seperti max berfungsi untuk mencari angka tapi ini mencari angka terkecil 
print(min(4,4,2,4,5,7,1,13,23,5,90,0,2)) # bisa mencari angka terkecil secara manual
a = [1,3,5,2,4,7,1,5,6,9]
print(min(a)) # bisa mencari angka terkecil dalam list
print()


# Module Math / Import Math

import math

# math.sqrt()
# berfungsi untuk menghitung akar
print(math.sqrt(25)) # akar 25
print(math.sqrt(16)) # akar 16
print()


# math.ceil() dan math.floor()
# math.ceil() berfungsi pembulatan ke atas
# math.floor() berfungsi pembulatan ke bawah
print(math.ceil(3.14))
print(math.floor(0.5))
print()


# math.pi
# ini adalah nilai pi yang berguna untuk menghitung luas dan keliling bidang lingkaran, dan geometri
print(round(math.pi, 2))
















