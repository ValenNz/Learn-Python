# uji_coba.py - Eksperimen print vs return

def luas_cetak(p, l):
    print(p * l)

def luas_hitung(p, l):
    return p * l

print("--- Uji luas_cetak ---")
a = luas_cetak(3, 4)
print("Isi variabel a:", a)
print("Tipe data a:", type(a))

print("\n--- Uji luas_hitung ---")
b = luas_hitung(3, 4)
print("Isi variabel b:", b)
print("Tipe data b:", type(b))
print("b + 10 =", b + 10)