# latihan5.py
# Fungsi rekursif: faktorial dan hitung mundur

def faktorial(n):
    if n == 0:          # <-- Base case
        return 1
    return n * faktorial(n - 1)   # <-- Recursive case

def hitung_mundur(n):
    if n == 0:          # <-- Base case
        print("Mulai!")
    else:               # <-- Recursive case
        print(n)
        hitung_mundur(n - 1)

print("5! =", faktorial(5))
hitung_mundur(3)