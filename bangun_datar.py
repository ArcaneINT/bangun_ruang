import math

def hk_bola(r):
    return 2 * math.pi * r

def hl_bola(r):
    return 4 * math.pi * r ** 2

def hv_bola(r):
    return (4/3) * math.pi * r ** 3

#-------------------------------------------------------------

def hk_kubus(s):
    return 12 * s

def hl_kubus(s):
    return 6 * s ** 2

def hv_kubus(s):
    return s ** 3

#-------------------------------------------------------------

def hk_balok(p, l, t):
    return 4 * (p + l + t)

def hl_balok(p, l, t):
    return 2 * (p * l + p * t + l * t)

def hv_balok(p, l, t):
    return p * l * t

print("Selamat datang di Program Hitung Bangun Ruang")
print("Pilihan utama:")
print("A) Bola")
print("B) Kubus")
print("C) Balok")
print("D) keluar")

while True:
    menu_hitung = input("Pilihan utama (a/b/c/d): ").lower()

    if menu_hitung == 'a':
        print("Pilihan untuk bola:")
        print("1. Keliling")
        print("2. Luas")
        print("3. Volume")
        hitung_bola = input("Masukkan pilihan (1/2/3): ")
        r = float(input("Masukkan jari-jari bola: "))
        if hitung_bola == '1':
            print("Keliling bola:", hk_bola(r))
        elif hitung_bola == '2':
            print("Luas bola:", hl_bola(r))
        elif hitung_bola == '3':
            print("Volume bola:", hv_bola(r))
        else:
            print("Pilihan tidak valid")

    elif menu_hitung == 'b':
        print("Pilihan untuk kubus:")
        print("1. Keliling")
        print("2. Luas")
        print("3. Volume")
        pilihan_kubus = input("Masukkan pilihan (1/2/3): ")
        s = float(input("Masukkan panjang sisi kubus: "))
        if pilihan_kubus == '1':
            print("Keliling kubus:", hk_kubus(s))
        elif pilihan_kubus == '2':
            print("Luas kubus:", hl_kubus(s))
        elif pilihan_kubus == '3':
            print("Volume kubus:", hv_kubus(s))
        else:
            print("Pilihan tidak valid")

    elif menu_hitung == 'c':
        print("Pilihan untuk balok:")
        print("1. Keliling")
        print("2. Luas")
        print("3. Volume")
        pilihan_balok = input("Masukkan pilihan (1/2/3): ")
        p = float(input("Masukkan panjang balok: "))
        l = float(input("Masukkan lebar balok: "))
        t = float(input("Masukkan tinggi balok: "))
        if pilihan_balok == '1':
            print("Keliling balok:", hk_balok(p, l, t))
        elif pilihan_balok == '2':
            print("Luas balok:", hl_balok(p, l, t))
        elif pilihan_balok == '3':
            print("Volume balok:", hv_balok(p, l, t))
        else:
            print("Pilihan tidak valid")

    elif menu_hitung == 'd':
        print("Keluar Aplikasi")
        break

    else:
        print("Pilihan utama tidak valid")

    ulangi = input("Apakah ingin menghitung kembali? (ya/tidak): ").lower()
    if ulangi != 'ya':
        break
