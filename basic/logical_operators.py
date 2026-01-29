# LOGICAL OPERATOR 
# operator yang berfungsi memodifikasi atau mengombinasi suatu kondisi yang nantinya menghasilkan nilai True atau False
# operator logika di bagi menjadi 3 : 

# ================= AND ==================== #

# True and True   = True
# True and False  = False
# False and True  = False
# False and False = False
# akan menghasilkan nilai True jika kedua nilai True

# contoh 1
a = 3 # nilai a adalah 3
if (a > 1) and (a < 5): # jika a lebih dari 1 dan jika a kurang dari 5 maka:
    print(True) # akan True
else: # jika tidak maka:
    print(False) # akan False

# di atas ini kita bisa membuktikan bahwa True and True = True

# contoh 2
b = 2 # nilai b adalah 3
if (b > 3) and (b < 5): # jika b lebih dari 3 dan jika b kurang dari 5 maka:
    print(True) # akan True
else: # jika tidak maka:
    print(False) # akan False

# di atas ini kita bisa membuktikan bahwa True and False = False


# ================= OR ==================== #

# True or True   = True
# True or False  = True
# False or True  = True
# False or False = False
# akan menghasilkan nilai True jika terdapat 1 nilainya TRUE

# contoh 1 
a = 10 # nilai a adalah 10
if (a > 1) or (a < 5): # jika a lebih dari 1 atau a kurang dari 5 maka:
    print(True) # akan True 
else: # jika tidak maka:
    print(False) # akan False

# di atas ini kita bisa membuktikan bahwa True or False = True

# contoh 2 
a = 10 # nilai a adalah 10
if (a < 1) or (a < 5): # jika a kurang dari 1 atau a kurang dari 5 maka:
    print(True) # akan True 
else: # jika tidak maka:
    print(False) # akan False

# di atas ini kita bisa membuktikan bahwa False or False = False


# ================= NOT ==================== #

# False not  = True
# True  not  = False
# akan menghasilkan nilai True jika kedua nilai True

print(not True) # tidak True maka False
print(not False) # tidak False maka True









