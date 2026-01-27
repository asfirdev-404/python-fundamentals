# IF STATEMENT
# if statement adalah sebuah struktur kontrol yang di membuat keputusan atau percabangan dengan berdasarkan kondisi tertentu

# if statement ini di bagi jadi 2 bagian
# yaitu 2 kondisi (if dan else) dan lebih dari 2 kondisi (if, else, dan elif)

# contoh 2 kondisi
umur = 12 # umur 12
if umur > 17: # ini adalah kondisi "jika" umur lebih dari 17
    print("Anda boleh membuat SIM") # akan mengeluarkan output ini jika memenuhi kondisi "jika"
else: # ini adalah kondisi "jika tidak" ketika tidak memenuhi kondisi "jika"
    print("Anda belum cukup umur untuk membuat SIM") # akan mengeluarkan output "jika tidak"

# Di baca : Umur adalah 12, jika umur kamu lebih dari 17 maka "Anda boleh membuat SIM", jika tidak maka "Anda tidak cukup umur untuk membuat SIM", maka "Anda tidak cukup umur untuk membuat SIM"


# contoh lebih dari 2 kondisi
umur = 70 # umur 20
if umur > 60: # ini adalah kondisi "jika" umur lebih dari 60 tahun
    print("Lansia") # maka umur tersebut adalah "Lansia"
if 12 <= umur <= 18: # ini adalah kondisi "lain jika" umur di antara 12 sampai 18 
    print("Remaja") # maka umur tersebut adalah "Remaja"
if 19 <= umur <= 60: # ini adalah kondisi "lain jika" umur di antara 19 sampai 60 tahun
    print("Dewasa") # maka umur tersebut adalah "Dewasa"
if 5 <= umur <= 11: # ini adalah kondisi "lain jika" umur di antara 5 sampai 11 tahun
    print("Anak-anak") # maka umur tersebut adalaha "Anak-anak"
else: # ini adalah kondisi ketika umur tidak termasuk dalam kondisi "jika" maupun "lain jika"
    print("Balita") # maka umur tersebut adalah "Balita"

# Di baca : Umur adalah 20, jika umur lebih dari 60 tahun maka disebut "Lansia", lain jika umur di antara 19 sampai 60 tahun maka di sebut "Dewasa", lain jika umur di antara 12 sampai 18 maka di sebut "Remaja", lain jika umut di antara 5 sampai 11 maka di sebut "Anak - anak", selain kondisi umur tadi maka di sebut "Balita"


