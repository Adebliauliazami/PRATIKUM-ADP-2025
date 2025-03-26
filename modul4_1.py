n = int(input("Masukkan jumlah baris: "))
m = int(input("Masukkan jumlah kolom: "))

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()