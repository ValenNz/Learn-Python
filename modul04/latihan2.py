# latihan2.py
# Fungsi yang mengembalikan nilai

def celsius_ke_fahrenheit(c):
    return c * 9 / 5 + 32

def luas_persegi_panjang(p, l):
    return p * l

# Konversi suhu
suhu = float(input("Suhu (Celsius): "))
f = celsius_ke_fahrenheit(suhu)
print("Fahrenheit:", f)

# Hitung luas dua ruangan
luas_kamar = luas_persegi_panjang(4, 3)
luas_dapur = luas_persegi_panjang(3, 2)
print("Luas kamar:", luas_kamar)
print("Luas dapur:", luas_dapur)
print("Total luas:", luas_kamar + luas_dapur)