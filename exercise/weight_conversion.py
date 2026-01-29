# WEIGHT CONVERSION
# convert berat kilogram ke pound atau pound ke kilogram

berat1 = float(input("Masukan nominal berat : "))
satuan = input("Kilogram atau Pound (K or L) : ")

if satuan == "K":
    berat2 = berat1 * 2.20462
    unit1 = "Kgs"
    unit2 = "Lbs"
    print(f"\nBerat anda {berat1}{unit1} di konversi menjadi {round(berat2, 2)}{unit2}")
elif satuan == "L":
    berat2 = berat1 / 2.20462
    unit1= "Lbs"
    unit2= "Kgs"
    print(f"\nBerat anda {berat1}{unit1} di konversi menjadi {round(berat2, 2)}{unit2}")
else:
    print("\nTolong masukan operator yang sesuai")
