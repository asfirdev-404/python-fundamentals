# ARITMATIKA
# aritmatika pada python sama seperti aritmatika pada umumnya yaitu operasi bilangan dasar

# contoh 
a = 8
b = 2
print(a+b)


# ada operasi bilangan yang lain meliputi :

# Pertambahan +
pertambahan = a + b # untuk menjumlahkan bilangan
print(f"\nHasil {a} + {b} = {pertambahan}")

# Pengurangan -
pertambahan = a - b # untuk pengurangan bilangan
print(f"\nHasil {a} - {b} = {pertambahan}")

# Perkalian *
pertambahan = a * b # untuk mengalikan bilangan
print(f"\nHasil {a} * {b} = {pertambahan}")

# Pembagian /
pertambahan = a / b # untuk membagi bilangan
print(f"\nHasil {a} / {b} = {pertambahan}")

# Modulus %
pertambahan = a % b # untuk mendapatkan bilangan sisa dari pembagian
print(f"\nHasil {a} % {b} = {pertambahan}")

# Pembagian bulat //
pertambahan = a // b # untuk membulatkan hasil bilangan yang di bagi
print(f"\nHasil {a} // {b} = {pertambahan}")

# Akar **
pertambahan = a ** b # untuk mengakar bilangan
print(f"\nHasil {a} ** {b} = {pertambahan}")


# ada operasi assigment gabungan (di singkat) :
# berfungsi untuk memudahkan cara penulisan 

# contoh 
a = 2
a += 2 # ini seperi a = a + 2
print(a) # memperbarui nilai a

# inti dari cara penulisan adalah (operasi bilangan)= 
# += -= *= /= %= //= **=


# urutan operasi (prioritas)
# ini adalah hal terpenting setelah mengetahui operasi bilangan yaitu urutan operasi

# 1. () → Kurung (dikerjakan dulu)
# 2. ** → Pangkat
# 3. *, /, //, % → Perkalian/pembagian (kiri ke kanan)
# 4. +, - → Penjumlahan/pengurangan (kiri ke kanan)

# contoh
hasil = (2 + 2) ** 2 % 3 * 4 / 5 + 2 - 7

# hasil = (2 + 2) ** 2 % 3 * 4 / 5 + 2 - 7
# hasil = 4 ** 2 % 3 * 4 / 5 + 2 - 7
# hasil = 16 % 3 * 4 / 5 + 2 - 7
# hasil = 1 * 4 / 5 + 2 - 7
# hasil = 4 / 5 + 2 - 7
# hasil = 0.8 + 2 - 7
# hasil = 2.8 - 7
# hasil = -4.2

print(hasil)








