data = """
Budi,123456,IF-45,ketua acara;anggota danus,85,Acara
Siti,789012,IF-45,anggota acara;anggota pubdok,90,Pubdok
Andi,345678,IF-45,ketua pubdok;anggota acara,88,Pubdok
Rina,567890,IF-45,anggota perlengkapan;anggota acara,75,Perlengkapan
Dewi,654321,IF-45,ketua danus;anggota pubdok,80,Danus
Yoga,432198,IF-45,anggota acara;anggota perlengkapan,92,Acara
Tono,321654,IF-45,anggota danus;anggota pubdok,78,Danus
Citra,876543,IF-45,anggota pubdok;anggota acara,84,Pubdok
"""

with open("OrPSB22.txt", "w") as file:
    file.write(data)

def baca_file(nama_file):
    data = []
    with open(nama_file, 'r') as file:
        for baris in file:
            nama, nim, kelas, pengalaman, wawancara, bidang = baris.strip().split(',')
            pengalaman = pengalaman.lower().split(';')
            data.append({
                'nama': nama,
                'nim': nim,
                'kelas': kelas,
                'pengalaman': pengalaman,
                'nilai_wawancara': int(wawancara),
                'bidang': bidang.lower()
            })
    return data

def hitung_nilai(cakoor):
    tambahan = 0
    for pengalaman_item in cakoor['pengalaman']:
        if 'ketua' in pengalaman_item:
            tambahan += 2
        if cakoor['bidang'] in pengalaman_item:
            tambahan += 3
            break
    return cakoor['nilai_wawancara'] + tambahan

def seleksi_koordinator(data):
    bidang_dict = {}
    for orang in data:
        nilai = hitung_nilai(orang)
        bidang = orang['bidang']
        if bidang not in bidang_dict:
            bidang_dict[bidang] = []
        bidang_dict[bidang].append((nilai, orang['nama']))
    
    hasil = {}
    for bidang, peserta in bidang_dict.items():
        peserta.sort(reverse=True)
        hasil[bidang] = peserta[:2]
    return hasil

data_cakoor = baca_file("OrPSB22.txt")
hasil_koor = seleksi_koordinator(data_cakoor)

with open("hasil_seleksi.txt", "w") as hasil:
    hasil.write("=== Hasil Seleksi Koordinator Tiap Bidang ===\n\n")
    for bidang, koors in hasil_koor.items():
        hasil.write(f"Bidang {bidang.title()}:\n")
        for i, (nilai, nama) in enumerate(koors, 1):
            hasil.write(f"  {i}. {nama} (Nilai: {nilai})\n")
        hasil.write("\n")

with open("hasil_seleksi.txt", "r") as hasil:
    print(hasil.read())
