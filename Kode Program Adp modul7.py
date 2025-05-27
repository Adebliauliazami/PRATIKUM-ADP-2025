def hitung_glbb(v0, a, t):
    v = v0 + a * t  
    s = v0 * t + 0.5 * a * t**2  
    return v, s

print()
print("1.3. OUTPUT ")
print()
n = int(input("Masukkan jumlah data (n): "))

v0_list = []
a_list = []
t_list = []
v_list = []
s_list = []
print()

for i in range(n):
    print(f"Data ke-{i+1}")
    v0 = float(input("Kecepatan awal (m/s): "))
    a = float(input("Percepatan (m/s²): "))
    t = float(input("Waktu (s): "))
    print()
    v, s = hitung_glbb(v0, a, t)


    v0_list.append(v0)
    a_list.append(a)
    t_list.append(t)
    v_list.append(v)
    s_list.append(s)

print("Hasil Perhitungan:")
print("+----+----------------+-------------+--------+------------------+-----------+")
print("| n  | Kecepatan Awal | Percepatan  | Waktu  | Kecepatan Akhir  |   Jarak   |")
print("|    |     (m/s)      |   (m/s²)    |  (s)   |      (m/s)       |    (m)    |")
print("+----+----------------+-------------+--------+------------------+-----------+")

for i in range(n):
    print(f"| {i+1:<2} | {v0_list[i]:<14.2f} | {a_list[i]:<11.2f} | {t_list[i]:<6.2f} | {v_list[i]:<16.2f} | {s_list[i]:<9.2f} |")

print("+----+----------------+-------------+--------+------------------+-----------+")
