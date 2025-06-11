import time
import os
from termcolor import colored

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ------------------ Fungsi Logo Pertamina ------------------
def tampil_logo_pertamina():
    logo = [
        "         " + colored("   ████", 'red') + "    " + colored("██████╗ ███████╗██████╗ ████████╗ █████╗ ███╗   ███╗██╗███╗   ██╗ █████╗", 'black'),
        "          " + colored("   ████", 'red') + "   " + colored("██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗", 'black'),
        "        " + colored("████", 'blue') + colored(" ████", 'green') + "  " + colored(" ██████╔╝█████╗  ██████╔╝   ██║   ███████║██╔████╔██║██║██╔██╗ ██║███████║", 'black'),
        "       " + colored("████", 'blue') + colored(" ████", 'green') + " " + colored("   ██╔═══╝ ██╔══╝  ██╔══██╗   ██║   ██╔══██║██║╚██╔╝██║██║██║╚██╗██║██╔══██║", 'black'),
        "      " + colored("████", 'blue') + "       " + colored("   ██║     ███████╗██║  ██║   ██║   ██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║", 'black'),
        "                    " + colored("╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝", 'black')
    ]
    
    for i in range(len(logo)):
        clear()
        for j in range(i + 1):
            print(logo[j])
        time.sleep(0.3)

    nama = input("Masukkan Tanggapan Anda : ")
    with open("Kritikan_logo.txt", "w", encoding="utf-8") as f:
        f.write(f"Kritikan nya : {nama}")
    print("Disimpan ke file 'Kritikan_logo.txt'")
    input("Tekan Enter untuk kembali ke menu...")

def logo_satu_susunan(simbol):
    hasil = []
    for i in range(10):
        spasi_awal = (9 - i) * 3
        line = " " * spasi_awal
        for j in range(i + 1):
            line += colored(simbol * 3, "black") + " "
        hasil.append(line)
    return hasil

huruf_balok = {
    "A": [
        "  ██  ",
        " █  █ ",
        "██████",
        "█    █",
        "█    █"
    ],
    "D": [
        "█████ ",
        "█    █",
        "█    █",
        "█    █",
        "█████ "
    ],
    "I": [
        "█████",
        "  █  ",
        "  █  ",
        "  █  ",
        "█████"
    ],
    "S": [
        " █████",
        "█     ",
        " ████ ",
        "     █",
        "█████ "
    ]
}

def cetak_teks_balok(teks):
    teks = teks.upper()
    for baris in range(5):
        line = ""
        for huruf in teks:
            if huruf in huruf_balok:
                line += colored(huruf_balok[huruf][baris], "black") + "  "
            else:
                line += "      "
        print(line)
        time.sleep(0.1)

def tampil_logo_adiids():
    simbol = "█"
    logo = logo_satu_susunan(simbol)
    clear()
    print("")
    for baris in logo:
        print(baris)
        time.sleep(0.2)
    print("")
    cetak_teks_balok("adidas")

    nama = input("Masukkan Tanggapan Anda : ")
    with open("Kritikan_logo.txt", "w", encoding="utf-8") as f:
        f.write(f"Kritikan nya : {nama}")
    print("Disimpan ke file 'Kritikan_logo.txt'")
    input("Tekan Enter untuk kembali ke menu...")
    
def main():
    while True:
        clear()
        print("=== PROGRAM LOGO PILIHAN ===")
        print("[1] Tampilkan Logo Pertamina")
        print("[2] Tampilkan Logo adiids")
        print("[3] Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            tampil_logo_pertamina()
        elif pilihan == "2":
            tampil_logo_adiids()
        elif pilihan == "3":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(1)

if __name__ == "__main__":
    main()
