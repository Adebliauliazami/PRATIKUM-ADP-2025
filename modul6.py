konversi_nilai = {
    "A": 4.00,
    "A-": 3.75,
    "B+": 3.50,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.00,
    "D": 1.00,
    "E": 0.00
}

jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

nilai_mahasiswa = []

for i in range(jumlah_mahasiswa):
    print(f"Mahasiswa ke-{i+1}")
    nilai_per_mahasiswa = []
    for j in range(jumlah_matkul):
        nilai = input(f"  Nilai mata kuliah ke-{j+1}: ").upper()
        while nilai not in konversi_nilai:
            print("  Nilai tidak valid! Masukkan lagi.")
            nilai = input(f"  Nilai mata kuliah ke-{j+1}: ").upper()
        nilai_per_mahasiswa.append(nilai)
    nilai_mahasiswa.append(nilai_per_mahasiswa)

data_ipk = []
for i in range(jumlah_mahasiswa):
    total_ip = 0
    for j in range(jumlah_matkul):
        huruf = nilai_mahasiswa[i][j]
        total_ip += konversi_nilai[huruf]
    ipk = total_ip / jumlah_matkul
    data_ipk.append([f"Mahasiswa-{i+1}", ipk])

for i in range(len(data_ipk) - 1):
    for j in range(len(data_ipk) - i - 1):
        if data_ipk[j][1] < data_ipk[j + 1][1]:
            data_ipk[j], data_ipk[j + 1] = data_ipk[j + 1], data_ipk[j]

print("Daftar IP Mahasiswa (dari tertinggi ke terendah):")
print("+-----------------+-------+")
print("| {:<15} | {:<5} |".format("Nama", "IPK"))
print("+-----------------+-------+")
for data in data_ipk:
    print("| {:<15} | {:.2f}  |".format(data[0], data[1]))
print("+-----------------+-------+")