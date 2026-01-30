# INDEXING 
# berfungsi untuk menegeluarkan output string secara detail
# cara penggunaan : 
# data[awal:akhir:step]

data = "0813-8686-0107"
print(data)
print(data[0]) # dalam indexing bilangan pertama atau penyebut pertama itu urutannya adalah 0
print(data[-1]) # dalam indexing bilangan akhir itu bisa juga di tulis -1 jika terlalu banyak
print(data[0:4]) # dalam indexing juga penyebut terakhir itu seperti perhitungan urutan pada normalnua
print(data[:4]) # bisa juga di tulis seperti ini karena awal atau akhir jika tidak di isi maka itu mempresentasikan ujung dari variable itu
print(data[::2]) # ini akan mengeluarkan data ujung awal dan ujung akhir tapi di loncati setiap 2 bilangan (karena tadi kita sudah menjelaskan bahwa jika bilangan awal atau akhir kosong itu mempresentasikan ujungnya)

# contoh 
text = "Python2025Programming"

# TUGAS KAMU:
# Pakai INDEXING/SLICING untuk output:
# "2025"


# Tulis jawaban kamu:
result = text[6:10]

print(result)  # Harus output: 2025

