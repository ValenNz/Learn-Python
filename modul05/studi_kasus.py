# === DEFINISI FUNGSI ===

def hitung_rata(data):
    """Plan Akumulator untuk menghitung rata-rata"""
    total = 0
    for x in data:
        total = total + x
    return total / len(data)

def cari_tertinggi(data):
    """Plan Nilai Ekstrem, mengembalikan tuple (nilai, indeks)"""
    terbesar = data[0]
    idx_terbesar = 0
    
    for i in range(len(data)):
        if data[i] > terbesar:
            terbesar = data[i]
            idx_terbesar = i
            
    return (terbesar, idx_terbesar)

def cari_nama(daftar, target):
    """Pencarian linier berpenanda, mengembalikan indeks atau -1"""
    posisi = -1
    i = 0
    while i < len(daftar) and posisi == -1:
        if daftar[i] == target:
            posisi = i
        i = i + 1
    return posisi

def hitung_lulus(data):
    """Tantangan Tambahan: Mengembalikan tuple (jumlah_lulus, jumlah_remedial)"""
    jumlah_lulus = 0
    jumlah_remedial = 0
    for x in data:
        if x >= 70:
            jumlah_lulus += 1
        else:
            jumlah_remedial += 1
    return (jumlah_lulus, jumlah_remedial)


# === PROGRAM UTAMA ===

n = int(input("Jumlah mahasiswa: "))
nama = []
nilai = []

# Mengisi list nama dan nilai
for i in range(n):
    n_mhs = input("Nama: ")
    n_nilai = float(input("Nilai: "))
    nama.append(n_mhs)
    nilai.append(n_nilai)

# 1. Cetak Rata-rata kelas
rata = hitung_rata(nilai)
print(f"Rata-rata kelas: {round(rata, 2)}")

# 2. Cetak Nilai tertinggi beserta pemiliknya (Unpacking Tuple)
tinggi, idx = cari_tertinggi(nilai)
print(f"Nilai tertinggi: {tinggi} oleh {nama[idx]}")

# 3. Cetak daftar mahasiswa yang perlu remedial
print("Perlu remedial (nilai < 70):")
ada_remedial = False
for i in range(len(nilai)):
    if nilai[i] < 70:
        print(f"- {nama[i]}({nilai[i]})")
        ada_remedial = True
        
if not ada_remedial:
    print("- tidak ada")

# 4. Cari nama mahasiswa
cari = input("Cari nama mahasiswa: ")
idx_cari = cari_nama(nama, cari)

if idx_cari == -1:
    print("Nama tidak terdaftar")
else:
    print(f"{cari} mendapat nilai {nilai[idx_cari]}")

# 5. Tantangan Tambahan: Persentase Kelulusan
j_lulus, j_remedial = hitung_lulus(nilai)
persentase_lulus = (j_lulus / len(nilai)) * 100
print(f"Persentase kelulusan kelas: {round(persentase_lulus, 2)}%")