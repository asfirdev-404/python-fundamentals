# CONDITIONAL EXPRESSION EXERCISE

# Kasus 1: Cek Dewasa
# Bikin variable 'kategori' pakai conditional expression
# Kalau umur >= 18 → "Dewasa"
# Kalau umur < 18 → "Anak-anak"
umur = 15

kategori = "Dewasa" if umur >= 18 else "Anak-anak"
print(kategori)


# Kasus 2: Diskon Member
# Member dapat diskon 10%, non-member 0%
total_belanja = 100000
is_member = True

diskon = 0.1 if is_member == True else 0

print(f"Diskon: {diskon * 100}%")


# Kasus 3: Status Kelulusan
# Nilai >= 60 → "Lulus"
# Nilai < 60 → "Tidak Lulus"
nilai = 1

status = "Lulus" if nilai >= 60 else "Tidak lulus"

print(status)  


# Kasus 4: Harga Tiket
# Anak (<12 tahun): Rp 25.000
# Dewasa (>=12 tahun): Rp 50.000
# Pakai conditional expression
umur = 34

harga = 25000 if umur < 12 else 50000

print(f"Harga tiket: Rp {harga:,}") 


# Kasus 6: Validasi Username
# Kalau username ada isinya → pakai username
# Kalau kosong → pakai "Guest"
username = "fir"

display_name = username if username != "" else "Guest"

print(f"Welcome, {display_name}!")  



