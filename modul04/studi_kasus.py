# studi_kasus.py
# Kalkulator Nilai Akhir Mahasiswa dengan validasi input

# ===== DEFINISI FUNGSI =====

def nilai_valid(n):
    """Memeriksa apakah nilai berada di rentang 0 sampai 100."""
    return 0 <= n <= 100

def baca_nilai(label):
    """Membaca nilai dan mengulang selama tidak valid."""
    while True:
        nilai = float(input(label))
        if nilai_valid(nilai):
            return nilai
        else:
            print("Nilai harus 0 sampai 100.")

def nilai_akhir(tugas, uts, uas):
    """Menghitung Nilai Akhir sesuai bobot."""
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

def nilai_huruf(na):
    """Menentukan nilai huruf berdasarkan Nilai Akhir."""
    if na >= 85:
        return "A"
    elif na >= 70:
        return "B"
    elif na >= 55:
        return "C"
    else:
        return "D"

def rata_rata(total, banyak):
    """Menghitung rata-rata, aman terhadap pembagian dengan nol."""
    if banyak == 0:
        return 0
    return total / banyak

# ===== PROGRAM UTAMA =====

jumlah_mhs = int(input("Jumlah mahasiswa: "))
total_lulus = 0
total_na = 0

for i in range(jumlah_mhs):
    print(f"\n--- Mahasiswa ke-{i + 1} ---")
    nama = input("Nama: ")
    tugas = baca_nilai("Nilai tugas: ")
    uts = baca_nilai("Nilai UTS: ")
    uas = baca_nilai("Nilai UAS: ")
    
    na = nilai_akhir(tugas, uts, uas)
    huruf = nilai_huruf(na)
    
    print(f"{nama} -> NA: {round(na, 2)} | Huruf: {huruf}")
    
    total_na += na
    if na >= 55:
        total_lulus += 1

print(f"\n===== REKAP =====")
print(f"Jumlah lulus: {total_lulus} dari {jumlah_mhs}")
print(f"Rata-rata NA : {round(rata_rata(total_na, jumlah_mhs), 2)}")