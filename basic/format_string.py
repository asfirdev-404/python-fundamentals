# FORMAT STRING
# berfungsi untuk menggabungkan variable dengan text string

# f-string
a = 123
print(f"Angka : {a}") # f disini berfungsi sebagai penggabung variable dengan test string

# format()
nama = "Pang"
umur = 13
print("Nama ku adalah {0}, dan umur aku {1}".format(nama,umur)) # menggabungkan berdasarkan index data dari format



# Number formatting

# desimal
data1 = 3.14159
data2 = 2000.0
data3 = 1.5

print(f"{data1:.2f}") # ini membuat bilangan menjadi bilangan desimal 2
print(f"{data2:.0f}") # ini membuat bilangan tidak menjadi bilangan desimal
print(f"{data3:.2f}\n") # ini membuat bilangan menjadi 2 desimal walau hanya 1 desimal

# thousend separator
data1 = 3000
data2 = 15000
data3 = 19000000

print(f"{data1:,}") # sama seperti judulnya berfungsi memisahkan angka setelah kelipatan ke 3
print(f"{data2:,}") # bisa pakai koma ","
print(f"{data3:_}\n") # bisa pakai underscrore "_"

# kombinasi number formatting & thousend separator
data1 = 3000.14159
data2 = 2000.0
data3 = 1010101.5

print(f"{data1:,.2f}") 
print(f"{data2:,.0f}") 
print(f"{data3:_.2f}\n") 



# Padding & alignment

# align kiri/tengah/kanan
data = "Bambang"

print(f'"{data:>20}"')
print(f'"{data:^20}"')
print(f'"{data:<20}"\n')

# padding
data = "Bambang"

print(f'"{data:020}"')
print(f'"{data:020}"')
print(f'"{data:020}"')

