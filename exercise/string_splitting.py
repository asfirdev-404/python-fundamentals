# STRING SPLITTING
# berfungsi memisahkan username dengan domainnya

# contoh splitting emain
email = input("Masukan email untuk memisahkan username dengan domain : ")

username = email[:email.index("@")]
domain = email[email.index("@"):]
print(f"Usernamenya adalah {username} dan domainnya adalah {domain}")