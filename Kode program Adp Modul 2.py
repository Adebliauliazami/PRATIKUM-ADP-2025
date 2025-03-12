print("Daftar Film yang Sedang Tayang:")
print("1. Toy Story 3 - Rp55.000")
print("2. Cars 3 - Rp40.000")
print("3. Spider-Man - Rp60.000")
print("4. Frozen 2 - Rp50.000")
print("5. Fast And Furious 10 - Rp75.000")

nama = input("Masukkan nama Anda: ")
kode_film = input("Masukkan kode film yang ingin dibeli (1-5): ")
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dibeli: "))

if kode_film == "1":
    judul_film = "Toy Story 3"
    harga_tiket = 55000
elif kode_film == "2":
    judul_film = "Cars 3"
    harga_tiket = 40000
elif kode_film == "3":
    judul_film = "Spider-Man"
    harga_tiket = 60000
elif kode_film == "4":
    judul_film = "Frozen 2"
    harga_tiket = 50000
elif kode_film == "5":
    judul_film = "Fast And Furious 10"
    harga_tiket = 75000
else:
    print("Kode film tidak valid.")

total_harga = harga_tiket * jumlah_tiket

diskon = 0
if total_harga > 250000:
    diskon = 0.35
elif total_harga > 100000:
    diskon = 0.15

potongan_harga = total_harga * diskon
total_setelah_diskon = total_harga - potongan_harga

print("=== STRUK PEMBELIAN TIKET BIOSKOP ===")
print(f"Nama          : {nama}")
print(f"Judul Film    : {judul_film}")
print(f"Jumlah Tiket  : {jumlah_tiket}")
print(f"Harga Satuan  : Rp{harga_tiket}")
print(f"Potongan Harga: Rp{int(potongan_harga)}")
print(f"Total Harga   : Rp{int(total_setelah_diskon)}")
print("===================================")