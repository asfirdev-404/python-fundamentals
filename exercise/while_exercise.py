# WHILE LOOP EXERCISE

# KASUS 1
# Bikin program ATM sederhana:
# - Saldo awal: Rp 1.000.000
# - User bisa tarik uang berkali-kali
# - Kalau saldo habis atau user ketik "selesai" → stop
# - Tampilkan sisa saldo setiap transaksi

# saldo = 1000000

while True:
    menu= input("\nMau narik uang atau keluar (N or Q) : ")
    menu = menu.upper()
    if menu == "N":
        tarik = int(input("\nMau narik berapa : "))
        if tarik <= saldo:
            if tarik > 1000:
                saldo = saldo - tarik
                print()
                print("="*20)
                print("Saldo berhasil di tarik!")
                print(f"Sisa saldo rp. {saldo:,}")
                print("="*20)
            else:
                print("Minimal penarikan sebesar Rp 1,000")
        else:
            print("Maaf saldo tidak cukup!")
    elif menu == "Q":
        print(f"\nTerima kasih! Saldo akhir: Rp. {saldo:,}")
        break
    else:
        print("Tolong pilih dengan benar\n")


# 🎯 KASUS 2: Guess The Number (Medium)

# Bikin game tebak angka:
# - Program random angka 1-100
# - User tebak sampai benar
# - Kasih hint "Terlalu besar" atau "Terlalu kecil"
# - Hitung berapa kali tebak
# - Ada maksimal 7 kali tebak (kalau gagal → game over)

import random

angka_tebakan = random.randint(1,100)
print("GAME TEBAKAN ANGKA 1-100")
kesempatan = 7

while True:
    angka_input = int(input(f"Masukan angka tebakan dalam {kesempatan} kesempatan menebak : "))
    print()
    if kesempatan == 0:
        print("Anda gagal kesempatan anda habis")
        break
    elif (angka_input > angka_tebakan) and kesempatan != 0:
        print("Cobalah pilih angka lebih kecil")
        print()
        kesempatan -= 1
    elif angka_input < angka_tebakan and kesempatan != 0:
        print("Cobalah pilih angka lebih besar")
        print()
        kesempatan -= 1
    elif angka_input == angka_tebakan:
        print()
        print("!!! Selamat anda berhasil menebak angka !!!")
        print(f"Angka tebakan anda                              : {angka_input}")
        print(f"Anda masih memiliki kesempatan menebak dalam    : {kesempatan} kesempatan")
        break
    else:
        print("tolong masukan angka dengan benar")
    