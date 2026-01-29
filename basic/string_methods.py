# STRING METHODS
# berfungsi untuk memanipulasi dan operasi pada tipe data string


# len()
# berfungsi untuk menghitung string
data = input("Masukan teks untuk mengetahui berapa jumlah dari teks ini : ")
output = len(data)
print(f"Jumlahnya ada : {output}\n")

# find()
# berfungsi untuk mencari posisi substring berdasarkan index
data = input("Masukan teks untuk mengetahui posisi substring yang di cari : ")
search = input("Masukan sesuatu yang ingin anda cari dari teks sebelumnya : ")
output = data.find(search)
print(f"Hasilnya ada : {output}\n") # output akan -1 jika substring yang di cari tidak ada

# rfind()
# sama seperti find() tetapi posisi mencarinya dimulai dari kanan
data = input("Masukan teks untuk mengetahui posisi substring dari kanan yang di cari : ")
search = input("Masukan sesuatu yang ingin anda cari dari teks sebelumnya : ")
output = data.rfind(search)
print(f"Hasilnya ada : {output}\n") # sama seperti find() output akan -1 jika yang di cari tidaka ada

# index() 
# sama persis seperti find() tetapi jika yag di cari tidak ada maka akan eror output nya
data = input("Masukan teks untuk mengetahui posisi substring yang di cari : ")
search = input("Masukan sesuatu yang ingin anda cari dari teks sebelumnya : ")
output = data.index(search)
print(f"Hasilnya ada : {output}\n") # outpur akan eror jika yang di cari tidak sesuai

# count()
# berfungsi untuk mencari jumlah dari string
data = input("Masukan teks untuk mengetahui berapa jumlah yang di cari dari teks ini : ")
search = input("Masukan sesuatu yang ingin anda cari dari teks sebelumnya : ")
output = data.count(search)
print(f"Jumlahnya ada : {output}\n") 

# strip()
# berfungsi untuk clear atau menghapus spasi di awal dan di akhir jika ada
data = input("Masukan teks untuk menghapus spasi yang ada : ")
output = data.strip()
print(f"Hasilnya adalah : {output}\n") 

# lower()
# berfungsi untuk mengubah semua string menjadi huruh kecil
data = input("Masukan teks untuk mengubah semua huruh mejadi kecil : ")
output = data.lower()
print(f"Hasilnya adalah : {output}\n") 

# upper()
# berfungsi untuk mengubah semua string menjadi huruh besar
data = input("Masukan teks untuk mengubah semua huruh mejadi besar : ")
output = data.upper()
print(f"Hasilnya adalah : {output}\n") 

# capitalize()
# berfungsi untuk mengubah huruf awalan menjadi besar
data = input("Masukan teks untuk mengubah awalan kalimat : ")
output = data.capitalize()
print(f"Hasilnya adalah : {output}\n") 

# Title()
# berfungsi untuk mengubah huruf awalan menjadi besar setiap spasi
data = input("Masukan teks untuk mengubah setiap spasi menjadi huruh besar: ")
output = data.title()
print(f"Hasilnya adalah : {output}\n")

# startswith()
# berfungsi untuk menanyakan apakah benar awalan kata menggunakan seperti yang di cari
data = input("Masukan teks untuk mengetahui apakah kalimat disini di awali seperti yang di cari : ")
search = input("Masukan sesuatu yang ingin anda cari dari teks : ")
output = data.startswith(search)
print(f"Hasilnya ada : {output}\n") 

# endswith()
# berfungsi untuk menanyakan apakah benar akhiran kata menggunakan seperti yang di cari
data = input("Masukan teks untuk mengetahui apakah kalimat disini di akhiri seperti yang di cari : ")
search = input("Masukan sesuatu yang ingin anda cari dari teks : ")
output = data.endswith(search)
print(f"Hasilnya ada : {output}\n") 

# replace()
# berfungsi untuk mengganti substring
data = input("Masukan teks : ")
search = input("Masukan teks untuk yang ingin di ganti : ")
replace= input("Masukan sesuatu yang ingin anda ubah dari teks : ")
output = data.replace(search, replace)
print(f"Hasilnya ada : {output}\n") 

# isdigit()
# berfungsi untuk menngonfirmasi apakah hanya ada angka dalam string
data = input("Masukan teks untuk mengetahui apakah kalimat disini hanya terdapat angka : ")
output = data.isdigit()
print(f"Hasilnya ada : {output}\n") 

# isalpha()
# berfungsi untuk menngonfirmasi apakah hanya ada angka dalam string
data = input("Masukan teks untuk mengetahui apakah kalimat disini hanya terdapat angka : ")
output = data.isalpha()
print(f"Hasilnya ada : {output}\n") 

# isalnum()
# berfungsi untuk menngonfirmasi apakah hanya ada angka dan alpha dalam string
data = input("Masukan teks untuk mengetahui apakah kalimat disini hanya terdapat angka : ")
output = data.isalnum()
print(f"Hasilnya ada : {output}\n") 

# islower()
# berfungsi untuk menngonfirmasi apakah ada huruhf kecil saja dalam string
data = input("Masukan teks untuk mengetahui apakah kalimat disini hanya terdapat  : ")
output = data.islower()
print(f"Hasilnya ada : {output}\n") 

# isupper()
# berfungsi untuk menngonfirmasi apakah hanya ada huruf besar saja dalam string
data = input("Masukan teks untuk mengetahui apakah kalimat disini hanya terdapat  : ")
output = data.isupper()
print(f"Hasilnya ada : {output}\n") 




















