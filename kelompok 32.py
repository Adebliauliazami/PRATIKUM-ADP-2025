from termcolor import colored, cprint 
import os 
import time

output_buku = {}
buku_dipinjam = {}

def animasi_loading():
    print(colored("Memulai sistem perpustakaan...", 'blue'))
    for i in range(25):
        print(colored(" █", 'blue'), end='', flush=True)
        time.sleep(0.1)
    print("\n" + colored("Sistem siap!", 'blue'))
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_status_rak():
    print("STATUS RAK:")
    lemari_list = ['A', 'B', 'C', 'D']
    for lemari in lemari_list:
        for rak in [1, 2]: 
            jumlah_buku = sum(1 for buku in output_buku.values() 
            if buku['Lokasi Buku'] == f"Lemari {lemari}, Rak {rak}")
            status = f"Lemari {lemari}, Rak {rak}: {jumlah_buku}/3 buku"
            if jumlah_buku >= 3:
                cprint(status, 'red')
            elif jumlah_buku == 0:
                cprint(status, 'yellow')
            else:
                cprint(status, 'green')
    print()

def tampilkan_denah():
    print()
    cprint(" "*15, 'white', 'on_black', end="") 
    cprint("           RUANG BACA           ", 'black', 'on_yellow', end="") 
    cprint(" "*15, 'white', 'on_black') 

    cprint(" "*15, 'white', 'on_black', end="") 
    for i in range(6): 
        cprint(" "*2, 'white','on_yellow', end="") 
        cprint(" "*3, 'white','on_red', end="") 
    cprint(" "*2,'white','on_yellow',end="") 
    cprint(" "*15,'white','on_black') 

    cprint(" "*15,'white','on_black',end="") 
    cprint(" "*32,'white','on_yellow',end="") 
    cprint(" "*15, 'white', 'on_black') 

    cprint(" "*15, 'white', 'on_black', end="") 
    for i in range(6): 
        cprint(" "*2, 'white','on_yellow', end="") 
        cprint(" "*3, 'white','on_red', end="") 
    cprint(" "*2,'white','on_yellow',end="") 
    cprint(" "*15,'white','on_black') 
    cprint(" "*15,'white','on_black',end="") 
    cprint(" "*32,'white','on_yellow',end="") 
    cprint(" "*15,'black','on_black') 

    cprint("                                                 PINTU MASUK ",'black','on_black',end="") 
    cprint(" ",'black','on_blue') 
    cprint(" "*61,'black','on_black',end="") 
    cprint(" ",'black','on_blue') 

    cprint(" "*15, 'white','on_black',end="") 
    cprint(" "*3, 'white','on_dark_grey',end="") 
    cprint(" "*3, 'white',"on_black",end="") 
    cprint("    A    ","white",'on_green',end="")     
    cprint(' '*3,"white",'on_black',end="") 
    cprint("    B    ","white",'on_green',end="") 
    cprint(" "*3, 'white',"on_black",end="") 
    cprint(" "*3, 'white','on_dark_grey',end="") 
    cprint(" "*14,'black',"on_black") 

    for i in range(3): 
        cprint(" "*15, 'white','on_black',end="") 
        cprint(" "*3, 'white','on_dark_grey',end="") 
        cprint(" "*27, 'white',"on_black",end="") 
        cprint(" "*3,"black","on_dark_grey",end="") 
        cprint(" "*14,"black","on_black") 
     
    cprint(" "*15, 'white','on_black',end="") 
    cprint(" "*3, 'white','on_dark_grey',end="") 
    cprint(" "*3, 'white',"on_black",end="") 
    cprint("    C    ","white",'on_green',end="")     
    cprint(' '*3,"white",'on_black',end="") 
    cprint("    D    ","white",'on_green',end="") 
    cprint(" "*3, 'white',"on_black",end="") 
    cprint(" "*3, 'white','on_dark_grey',end="") 
    cprint(" "*14,'black',"on_black")
    cprint(" "*15, 'white','on_black',end="") 
    cprint(" "*3, 'white','on_dark_grey',end="") 
    cprint(" "*3, 'white',"on_black",end="") 
    cprint(" "*24, 'white',"on_black",end="") 
    cprint(" "*3, 'white','on_dark_grey',end="") 
    cprint(" "*14,'black',"on_black") 

    cprint("KETERANGAN:", 'cyan')
    print(colored("  ██", 'white', 'on_green'), "= Lemari Rak")
    print(colored("  ██", 'white', 'on_red'), "= Meja Baca")
    print(colored("  ██", 'white', 'on_yellow'), "= Ruang Baca")
    print(colored("  ██", 'white', 'on_blue'), "= Pintu")

def tambah(): 
    judul = input("Masukkan Judul Buku  : ") 
    penulis = input("Masukkan Nama Penulis : ") 
    penerbit = input("Masukkan Nama Penerbit : ") 
    tahun_terbit = input("Masukkan Tahun Terbit : ") 
    
    while True:
        lokasi = input("Lokasi Buku (Contoh: Lemari A, Rak 1): ")
        if not lokasi.startswith(('Lemari A, Rak 1', 'Lemari B, Rak 1', 'Lemari C, Rak 1', 'Lemari D, Rak 1',
                                'Lemari A, Rak 2', 'Lemari B, Rak 2', 'Lemari C, Rak 2', 'Lemari D, Rak 2')):
            print("Error: Hanya Rak 1 dan Rak 2 yang tersedia di Lemari A, B, C, atau D")
            continue
        
        jumlah_di_rak = sum(1 for buku in output_buku.values() if buku['Lokasi Buku'] == lokasi)
        if jumlah_di_rak >= 3:
            print(f"Error: {lokasi} sudah penuh (3/3 buku). Pilih rak lain.")
        else:
            break

    output_buku[judul] = { 
        'Penulis': penulis, 
        'Penerbit': penerbit, 
        'Tahun Terbit': tahun_terbit, 
        'Lokasi Buku': lokasi,
        'Status': 'Tersedia'
    } 
    print("Data buku berhasil ditambahkan!") 
    tampilkan_status_rak()

def hapus(): 
    judul = input("Masukkan judul buku yang ingin dihapus : ") 
    if judul in output_buku: 
        del output_buku[judul] 
        print("Data buku berhasil dihapus!") 
    else: 
        print("Buku tidak ditemukan dalam daftar.") 

def tampilkan_buku(): 
    if not output_buku: 
        print("Belum ada data buku yang tersimpan.") 
    else: 
        print("Data Buku : ") 
        for judul, info in output_buku.items(): 
            print(f"Judul: {judul}") 
            print(f"Penulis: {info['Penulis']}") 
            print(f"Penerbit: {info['Penerbit']}") 
            print(f"Tahun Terbit: {info['Tahun Terbit']}") 
            print(f"Lokasi Buku: {info['Lokasi Buku']}") 
            print(f"Status: {info['Status']}") 
            print()

def simpan(nama): 
    with open(nama, 'w') as file:
        for judul, info in output_buku.items(): 
            file.write(f"{judul},{info['Penulis']},{info['Penerbit']},{info['Tahun Terbit']},{info['Lokasi Buku']},{info['Status']}\n") 
    
    with open("buku_dipinjam.txt", 'w') as file:
        for judul, info in buku_dipinjam.items():
            file.write(f"{judul},{info['Penulis']},{info['Penerbit']},{info['Tahun Terbit']},{info['Lokasi Buku']},{info['Status']}\n")

def cari_buku(judul, tampilkan_denah_flag=False): 
    hasil_pencarian = {k: v for k, v in output_buku.items() if judul.lower() in k.lower()} 
    if not hasil_pencarian: 
        print(f"Tidak ditemukan buku dengan judul '{judul}'.") 
    else: 
        print("Hasil Pencarian:")
        for buku_judul, buku_info in hasil_pencarian.items(): 
            print(f"Judul: {buku_judul}") 
            print(f"Penulis: {buku_info['Penulis']}") 
            print(f"Penerbit: {buku_info['Penerbit']}") 
            print(f"Tahun Terbit: {buku_info['Tahun Terbit']}") 
            print(f"Lokasi Buku: {buku_info['Lokasi Buku']}") 
            print(f"Status: {buku_info['Status']}") 
        
        if tampilkan_denah_flag:
            tampilkan_denah()

def muat(nama): 
    buku = {} 
    try: 
        with open(nama, 'r') as file: 
            for line in file: 
                data = line.strip().split(',') 
                if len(data) == 6: 
                    judul, penulis, penerbit, tahun_terbit, lokasi, status = data 
                    buku[judul] = { 
                        'Penulis': penulis, 
                        'Penerbit': penerbit, 
                        'Tahun Terbit': tahun_terbit, 
                        'Lokasi Buku': lokasi,
                        'Status': status
                    } 
    except FileNotFoundError: 
        with open(nama, 'w') as file:
            pass  
    return buku 

def muat_buku_dipinjam():
    buku = {}
    try:
        with open("buku_dipinjam.txt", 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 6:
                    judul, penulis, penerbit, tahun_terbit, lokasi, status = data
                    buku[judul] = {
                        'Penulis': penulis,
                        'Penerbit': penerbit,
                        'Tahun Terbit': tahun_terbit,
                        'Lokasi Buku': lokasi,
                        'Status': status
                    }
    except FileNotFoundError:
        with open("buku_dipinjam.txt", 'w') as file:
            pass
    return buku

import time

def pinjam_buku():
    nama_peminjam = input("Masukkan nama Anda: ")
    judul = input("Masukkan judul buku yang ingin dipinjam: ")
    
    if judul in output_buku:
        if output_buku[judul]['Status'] == 'Tersedia':
            tanggal_pinjam = time.strftime("%d/%m/%Y")
            
            hari, bulan, tahun = map(int, tanggal_pinjam.split('/'))
            hari += 7
            
            days_in_month = {
                1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }
            
            if hari > days_in_month[bulan]:
                hari -= days_in_month[bulan]
                bulan += 1
                if bulan > 12:  
                    bulan = 1
                    tahun += 1
            
            tanggal_kembali = f"{hari:02d}/{bulan:02d}/{tahun}"
            
            output_buku[judul]['Status'] = 'Dipinjam'
            
            if nama_peminjam not in buku_dipinjam:
                buku_dipinjam[nama_peminjam] = {}
            
            buku_dipinjam[nama_peminjam][judul] = {
                'Tanggal Pinjam': tanggal_pinjam,
                'Tanggal Kembali': tanggal_kembali
            }
            
            print(f"Buku '{judul}' berhasil dipinjam oleh {nama_peminjam}.")
            print(f"Tanggal Pinjam: {tanggal_pinjam}")
            print(f"Batas Pengembalian: {tanggal_kembali} (7 hari)")
        else:
            print(f"Buku '{judul}' sedang tidak tersedia.")
    else:
        print(f"Buku '{judul}' tidak ditemukan.")

def kembalikan_buku():
    nama_peminjam = input("Masukkan nama Anda: ")
    judul = input("Masukkan judul buku yang ingin dikembalikan: ")
    
    if nama_peminjam in buku_dipinjam:
        if judul in buku_dipinjam[nama_peminjam]:
            output_buku[judul]['Status'] = 'Tersedia'
            
            del buku_dipinjam[nama_peminjam][judul]
            
            if not buku_dipinjam[nama_peminjam]:
                del buku_dipinjam[nama_peminjam]
            
            print(f"Buku '{judul}' berhasil dikembalikan oleh {nama_peminjam}.")
        else:
            print(f"Buku '{judul}' tidak ditemukan dalam pinjaman {nama_peminjam}.")
    else:
        print(f"Tidak ada data pinjaman untuk {nama_peminjam}.")

def tampilkan_buku_dipinjam():
    if not buku_dipinjam:
        print("Tidak ada buku yang sedang dipinjam.")
    else:
        print("\n=== DAFTAR BUKU YANG DIPINJAM ===")
        for nama_peminjam, buku in buku_dipinjam.items():
            print(f"\nPeminjam: {nama_peminjam}")
            for judul, info in buku.items():
                detail_buku = output_buku.get(judul, {})
                print(f"\n  Judul Buku: {judul}")
                print(f"  Penulis: {detail_buku.get('Penulis', '-')}")
                print(f"  Penerbit: {detail_buku.get('Penerbit', '-')}")
                print(f"  Tahun Terbit: {detail_buku.get('Tahun Terbit', '-')}")
                print(f"  Tanggal Pinjam: {info.get('Tanggal Pinjam', '-')}")
                print(f"  Batas Kembali: {info.get('Tanggal Kembali', '-')}")
        print("\n" + "="*30 + "\n")

def menu_karyawan(nama): 
    while True: 
        print("Menu Karyawan:") 
        print("1. Tambah Buku") 
        print("2. Hapus Buku") 
        print("3. Lihat Daftar Buku") 
        print("4. Lihat Daftar Buku Dipinjam")
        print("5. Kembali ke Menu Utama") 
        pilihan = input("Pilih opsi (1-5): ") 

        if pilihan == '1': 
            tambah() 
            simpan(nama) 

        elif pilihan == '2': 
            hapus() 
            simpan(nama) 

        elif pilihan == '3': 
            tampilkan_buku() 
            tampilkan_status_rak()

        elif pilihan == '4':
            tampilkan_buku_dipinjam()

        elif pilihan == '5': 
            break 

        else: 
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.") 

def menu_pendatang(): 
    while True: 
        print("Menu Pendatang:") 
        print("1. Cari Buku") 
        print("2. Lihat Daftar Buku") 
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Kembali ke Menu Utama") 
        pilihan = input("Pilih opsi (1-5): ") 

        if pilihan == '1': 
            judul = input("Masukkan judul buku yang ingin dicari: ") 
            cari_buku(judul, tampilkan_denah_flag=True) 

        elif pilihan == '2': 
            tampilkan_buku() 

        elif pilihan == '3':
            pinjam_buku()

        elif pilihan == '4':
            kembalikan_buku()

        elif pilihan == '5': 
            break 

        else: 
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.") 

def main(): 
    global output_buku, buku_dipinjam
    nama_file = "output_buku.txt" 
    password_karyawan = "12345678" 
    
    clear_screen()
    print("=================================================") 
    print("|                SELAMAT DATANG                 |") 
    print("|             DI PERPUSTAKAAN MINI              |") 
    print("|                      AA                       |") 
    print("=================================================") 
    
    animasi_loading()
    output_buku = muat(nama_file)
    buku_dipinjam = muat_buku_dipinjam()

    while True: 
        print("=== Menu Utama ===") 
        print("Siapakah Anda ?") 
        print("1. Karyawan") 
        print("2. Pendatang") 
        print("3. Keluar") 
        pilihan = input("Masukkan Pilihan (1/2/3): ") 

        if pilihan == '1': 
            password = input("Masukkan kata sandi karyawan : ") 
            if password == password_karyawan: 
                menu_karyawan(nama_file) 
            else: 
                print("Kata sandi salah!") 

        elif pilihan == '2': 
            menu_pendatang() 

        elif pilihan == '3': 
            simpan(nama_file)
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa lagi!") 
            break 

        else: 
            print("Pilihan tidak valid. Silahkan pilih opsi yang benar.") 

if __name__ == "__main__": 
    main()