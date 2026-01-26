# INPUT
# sesuai dengan namanya input berfungsi untuk memasukan data 

# contoh
data = input("Masukan teks : ") # untuk memasukan input 
print(data) # untuk mengeluarkan output

# input juga bisa di sesuaikan dengan tipe data yang ingin dipakai sesuai kebutuhan 

# Input str
# untuk menginput tipe data str
nama = input("\nName : ")
print(type(nama)) # untuk membuktikan bahwa input yang tersimpan adalah str
# peringatan : bisa input apa saja, hanya bisa cetak data, tidak untuk operasi aritmatika

# Input int
# untuk menginput tipe data int
umur = int(input("Umur : "))
print(type(umur)) # untuk membuktikan bahwa input yang tersimpan adalah int
# peringatan : hanya bisa cetak angka bulat saja selain itu akan eror, cocok untuk operasi aritmatika

# Input float
# untuk menginput tipe data float
tinggi_badan = float(input("Tinggi Badan : "))
print(type(tinggi_badan)) # untuk membuktikan bahwa input yang tersimpan adalah float
# peringatan : hanya bisa memasukan angka saja mau itu bilangan bulat maupun desimal, selain itu akan eror, cocok untuk operasi bilangan atau memberikan nilai dengan detail

# Input bool
# untuk menginput tipe data bool
meyakinkan = bool(input("Apakah kamu yakin dengan jawaban di atas (kosongkan jika yakin) : "))
print(meyakinkan)
print(type(meyakinkan)) # untuk membuktikan bahwa input yang tersimpan adalah str
# peringatan : input apa pun aka True selama tidak kosong   