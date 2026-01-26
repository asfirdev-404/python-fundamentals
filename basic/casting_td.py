# CASTING TIPE DATA
# casting tipe data sesuai dengan namanya adalah merubah sebuah nilai dari tipe data

# contoh dari tipe data integer ke tipe data string 
dataStr = "123"
print(type(dataStr)) # sebelum di ubah
dataStrtoInt = int(dataStr)
print(type(dataStrtoInt)) # setelah di ubah 

# jadi intinya cara mengubahnya itu dengan cara menggunakan singkatan tipe data 
# Integer   = int 
# Float     = float 
# String    = str
# Boolean   = bool

# caranya adalah singaktan_tipe_data_yang_ingin_di_ubah(variable)

# Integer for all casting
print("\nInteger for All Casting")
dataInt = 123
print(f"{dataInt} {type(dataInt)}")

# int to float
print(f"{float(dataInt)} {type(float(dataInt))}") # kalau dari int ke float maka akan di tambah .0 di belakangnya
# int to str
print(f"{str(dataInt)} {type(str(dataInt))}") # kalau dari int ke str maka tidak ada perubahan output tetapi tetap tidak bisa buat operasi aritmatika
# int to bool
print(f"{bool(dataInt)} {type(bool(dataInt))}") # kalau dari int ke boolean itu akan menghasilak output True atau False, jika int memberikan nilai angka tidak nol maka nilai yang keluar adalah True dan begitu sebaliknya 

# Float for all casting
print("\nFloat for All Casting")
dataFloat = 3.14
print(f"{dataFloat} {type(dataFloat)}")

# float to float
print(f"{int(dataFloat)} {type(int(dataInt))}") # kalau dari float ke int maka nilai tersebut akan di bulatkan 
# float to str
print(f"{str(dataFloat)} {type(str(dataInt))}") # kalau dari float ke str maka sama juga dengan int ke str, output tetap sama tetapi tidak bisa di gunakan untuk operasi aritmatika
# float to bool
print(f"{bool(dataFloat)} {type(bool(dataInt))}") # kalau dari float ke str maka sama juga dengan int ke bool, jika float memberikan nilai angka tidak nol maka nilai yang keluar adalah True dan begitu sebaliknya 

# String for all casting
print("\nString for All Casting")
dataStr = "123"
print(f"{dataStr} {type(dataStr)}")

# str to int
print(f"{int(dataStr)} {type(int(dataStr))}") # kalau dari str ke int maka nilai tersebut akan di ubah menjadi angka, tetapi jika str nya berupa huruf bukan angka maka akan eror
# str to int
print(f"{float(dataStr)} {type(float(dataStr))}") # kalau dari str ke float sama seperti int, tetapi beda dengan int bilangan ini akan di decimalkan jika bilangan tersebut bulat maka di tambahkan .0
# str to bool
print(f"{bool(dataStr)} {type(bool(dataStr))}") # kalau dari str ke bool maka hasilnya akan True jika str tersebut memberikan nilai, jika tidak memberikan nilai seperi "" maka hasil nilai boolnya akan False

# Boolean for all casting
print("\nBoolean for All Casting")
dataBool = 1
print(f"{dataBool} {type(dataBool)}")

# bool to int
print(f"{int(dataBool)} {type(int(dataBool))}") # kalau dari bool ke int hasilnya akan 1 jika True, akan 0 jika False
# bool to float
print(f"{float(dataBool)} {type(float(dataBool))}") # kalau dari bool ke float hasilnya akan 1.0 jika True, akan 0.0 jika False
# bool to str 
print(f"{str(dataBool)} {type(str(dataBool))}") # kalau dari bool ke str hasilnya akan 1 jika True, akan 0 jika False, tetapi angka ini nilai nya str tidak bisa di gunakan untuk proses aritmatika
















