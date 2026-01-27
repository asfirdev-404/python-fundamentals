# SIMPLE CALCULATOR
# membuat kalkulator sederhana

angka1 = float(input("Masukan angka pertama : "))
operator = input("Pilih Operator ( + | - | * | / ) : ") 
angka2 = float(input("Masukan angka kedua : "))

if operator == "+":
    hasil = angka1 + angka2
    print(f"\nHasilnya adalah = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"\nHasilnya adalah = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"\nHasilnya adalah = {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"\nHasilnya adalah = {hasil}")
else:
    print("\nTolong masukan operator dengan benar")