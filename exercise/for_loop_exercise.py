# FOR LOOP EXERCISE 

# level 1

# 1
for x in range(1,11):
    print(x)
print()
# 2
for x in range(1,11):
    if x % 2 == 1:
        continue
    print(x)
print()
# 3
hasil = 0
for x in range(1,11):
    hasil += x
print(hasil)

# level 2

# 1
nilai = [70, 85, 60, 90, 40, 88]
# 1
for x in nilai:
    print(x)
print()
2
total = 0
# 2
for x in nilai:
    total += x
rata_rata = total / len(nilai)
print(round(rata_rata, 2))
print()
# 3
for x in nilai:
    if x >= 75:
        print(x)
print()
# 4
jumlah_siswa_lulus = 0 
for x in nilai:
    if x >= 75:
        jumlah_siswa_lulus += 1
print(jumlah_siswa_lulus)


# level 3
text = "PythonForBeginner"

# 1
for x in text:
    print(x)
print()
# 2
jumlah_huruf = 0
for x in text:
    jumlah_huruf += 1
print(jumlah_huruf)
print()
# 3
huruf_vokal = ["a","i","u","e","o"]
jumlah_huruf_vokal = 0
for x in text.lower():
    if x in huruf_vokal:
        jumlah_huruf_vokal += 1
print(jumlah_huruf_vokal)
print()
# 4 
for x in text:
    if x == "F":
        break
    print(x)







