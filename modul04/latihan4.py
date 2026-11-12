# latihan4.py
# Menggunakan modul math dan random

import math
import random

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def lempar_dadu():
    return random.randint(1, 6)

# Hitung jarak dua titik
print("Jarak A ke B:", jarak(0, 0, 3, 4))
print("Jarak C ke D (dibulatkan ke atas):", math.ceil(jarak(1, 1, 4, 5.5)))

# Simulasi lempar dadu 3 kali
for i in range(3):
    print("Lemparan", str(i + 1) + ":", lempar_dadu())