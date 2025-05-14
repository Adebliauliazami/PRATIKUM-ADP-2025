while True:
    print("Program Perhitungan Fungsi")
    print("Output 1:")
    print("f(x) = 4x³ + 7x - 5, x > 0")
    print("     = 3x² - 5x + 1, x < 0")
    print("g(x) = (f(x))² - f(x)")
    print("h(x) = f(x) × g(x)\n")

    n = int(input("Input banyak data n: "))

    x = []
    f = []
    g = []
    h = []

    for i in range(n):
        xi = float(input(f"Input x ke-{i+1}: "))
        x.append(xi)

        if xi > 0 :
            fx = 4 * xi**3 + 7 * xi - 5
        elif xi < 0:
            fx = 3 * xi**2 - 5 * xi + 1
        else:
            fx = 0 

        gx = fx**2 - fx
        hx = fx * gx

        f.append(fx)
        g.append(gx)
        h.append(hx)

        print(f"f({xi}) = {fx}")
        print(f"g({xi}) = {gx}")
        print(f"h({xi}) = {hx}")
        print()

    print("Output 2:")
    Q = f"| {'No':<3} | {'x':<8} | {'f(x)':<15} | {'g(x)':<15} | {'h(x)':<15} |"
    R = "|-----|----------|-----------------|-----------------|-----------------|"
    print(Q)
    print(R)
    
    for i in range(n):
        S = f"| {i+1:<3} | {x[i]:<8.2f} | {f[i]:<15.2f} | {g[i]:<15.2f} | {h[i]:<15.2f} |"
        print(S)
    print()

    P = input("Input nilai x lagi? (Y/N): ").strip().upper()
    if P == 'N':
        print("Program selesai.")
        break
    elif P != 'Y':
        print("Jawaban tidak dikenali. Masukkan Y atau N.")
        break