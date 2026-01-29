# EXERCISE METHOD STRING

# 🧪 Kasus 1 — Validasi Username

# Buat program yang:
# Aturan:
# Input: username
# Jika username kosong → tampilkan "Username tidak boleh kosong"
# Jika username hanya huruf dan angka → "Username valid"
# Selain itu → "Username tidak valid"

username = input("Masukan username : ")
username = username.strip()
if username == "":
    print("Username tidak boleh kosong")
elif username.isalnum():
    print("Username valid")
else:
    print("Username tidak valid")


# 🧪 Kasus 2 — Akses Umur

# Buat program yang:
# Aturan:
# Input: umur (string dari input)
# Jika input bukan angka → "Input umur tidak valid"
# Jika angka:
# umur < 13 → "Anak-anak"
# umur 13–17 → "Remaja"
# umur ≥ 18 → "Dewasa"

umur = input("Masukan umur : ")
if not umur.isdigit():
    print("Input umur tidak valid")
else:
    umur = int(umur)
    if umur < 13:
        print("Anak-anak")
    elif 13 <= umur <= 17:
        print("Remaja")
    elif umur >= 18:
        print("Dewasa")


# 🧪 Kasus 3 — Cek Awalan & Akhiran

# Buat program yang:
# Aturan:
# Input: sebuah kalimat
# Jika diawali "Hello" dan diakhiri "!" → "Kalimat formal"
# Jika hanya salah satu yang terpenuhi → "Kalimat setengah formal"
# Jika tidak keduanya → "Kalimat santai"

kalimat = input("Masukan teks : ")
kalimat = kalimat.strip()

if kalimat.startswith("Hello") and kalimat.endswith("!"):
    print("Kalimat formal")
elif kalimat.startswith("Hello") or kalimat.endswith("!"):
    print("Kalimat setengah formal")
else:
    print("Kalimat santai")






