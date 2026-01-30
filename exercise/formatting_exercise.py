# Data
nama_toko = "MINIMARKET BERKAH"
item1 = "Indomie Goreng"
qty1 = 5
price1 = 3500

item2 = "Teh Botol"
qty2 = 3
price2 = 4000

item3 = "Oreo"
qty3 = 2
price3 = 12000

cashier = "Siti"
transaction_id = "TRX001"
total = (price1 * qty1) + (price2 * qty2) + (price3 * qty3)
ucapan = "TERIMA KASIH"

print("="*40)
print(f"{nama_toko:^40}")
print("="*40)
print(f"Transaction ID  : {transaction_id}")
print(f"Cashier         : {cashier}")
print("-"*40)
print(f"{item1:<20}{qty1} x Rp {price1:,}")
print(f"{item2:<20}{qty2} x Rp {price2:,}")
print(f"{item3:<20}{qty3} x Rp {price3:,}")
print("-"*40)
print(f"Subtotal             : Rp {total:,}")
print(f"Tax (11%)            : Rp {total * 0.11:,.0f}")
print(f"Total                : Rp {total +  (total * 0.11):,.0f}")
print("="*40)
print(f"{ucapan:^40}")
print("="*40)

# Student data
student_name = "Budi Santoso"
student_id = "2024001"
kelas = "12 IPA 1"

# Nilai
matematika = 85
fisika = 78
kimia = 92
biologi = 88
bahasa_inggris = 90
rata_rata = (matematika+fisika+kimia+biologi+bahasa_inggris)/5

report = f"""
╔═════════════════════════════════╗
║        RAPOR SEMESTER 1         ║
╠═════════════════════════════════╣
║ Nama     : {student_name:21}║
║ NIS      : {student_id:<21}║
║ Kelas    : {kelas:<21}║
╠═════════════════════════════════╣
║  MATA PELAJARAN         NILAI   ║
╠═════════════════════════════════╣
║ Matematika    {matematika:>14}    ║
║ Fisika        {fisika:>14}    ║        
║ Kimia         {kimia:>14}    ║
║ Biologi       {biologi:>14}    ║
║ Bahasa Inggris{bahasa_inggris:>14}    ║
╠═════════════════════════════════╣
║ Rata-rata     {rata_rata:>15}   ║
║ STATUS        {"LULUS" if rata_rata > 85 else "GAGAL":>16}  ║ 
╚═════════════════════════════════╝
"""
print(report)

file_name = "python_tutorial.mp4"
file_size_mb = 250.5
downloaded_mb = 187.875
download_speed_mbps = 5.2
server = "cdn.example.com"

a = 20
b = 15
c = a - b

dowload = f"""
┌──────────────────────────────────────────────┐
│              DOWNLOAD PROGRESS               │
├──────────────────────────────────────────────┤
│ File     : {file_name}               │
│ Server   : {server}                   │
│ Size     : {file_size_mb} MB                          │
├──────────────────────────────────────────────┤ 
│ Progress   : [{"█" * b + "░" * c}] 75.0%    │
│ Downloaded : {downloaded_mb} MB / {file_size_mb} MB           │
│ Speed      : {download_speed_mbps}                             │
│ Time       : 3m 0s                           │
│ Remaining  : 1m 0s                           │
├──────────────────────────────────────────────┤
│ Status   : DOWNLOADING...                    │
└──────────────────────────────────────────────┘

"""
print(dowload)








