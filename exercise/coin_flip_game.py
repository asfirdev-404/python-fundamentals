from random import choice

opsi = ("head","tail")
nyawa = 3
skor = 0

while True:
    coin = choice(opsi)
    print()
    print("Tebak tebakan coin flip, dapatkan skor sebanyak banyak nya")
    tebakan = input("pilih (head/tail) : ")
    tebakan = tebakan.lower()
    if (tebakan == coin) and (tebakan in opsi):
        print()
        print("Selamat anda benar")
        print(f"Skor +1")
        skor += 1
    elif nyawa == 0:
        print()
        print("================ - ================")
        print("Game Over!")
        print(f"Skor yang anda dapat : {skor}")
        print("================ - ================")
        break
    elif (tebakan != coin) and (tebakan in opsi):
        print()
        print("Maaf, anda salah")
        print(f"Silahkan coba lagi dalam kesempatan {nyawa}")
        nyawa -= 1
    else:
        print()
        print("Maaf input tidak dapat di proses")
        
        

