M = float(input("Masukkan Modal Awal Investasi : "))
r = float(input("Masukkan Suku bunga tahunan (%) : "))
T = float(input("Masukkan target investasi : "))

tahun = 0
while M <= T:
    M += M * (r / 100)
    tahun += 1
    print(f"Tahun ke-{tahun}: Rp{M}")
print(f"Target tercapai dalam {tahun} tahun! ")