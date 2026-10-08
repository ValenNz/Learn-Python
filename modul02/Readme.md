# 🔄 Modul Praktikum 2: Percabangan Bertingkat & Perulangan Dasar

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Sistem Informasi  
**Bahasa Pemrograman:** Python 3  
**Asisten Praktikum:** [Nama Anda]  

Selamat datang di sesi praktikum kedua! 🎉  
Di Modul 1, kita sudah belajar membuat program yang bisa "memilih" (if-else). Di Modul 2, kita akan meningkatkan levelnya: membuat program yang bisa **memilih secara bertingkat (nested if)** dan **mengulang tugas secara otomatis (looping)**. 

> ⚠️ **Catatan:** Untuk panduan instalasi Python, cara membuka terminal, dan shortcut VS Code, silakan baca **[README Universal di root folder](../Readme.md)**.

---

##  Daftar Isi
1. [Percabangan Bertingkat (Nested If)](#1-percabangan-bertingkat-nested-if)
2. [Konsep Dasar Perulangan (Looping)](#2-konsep-dasar-perulangan-looping)
3. [Perulangan `for` dan Fungsi `range()`](#3-perulangan-for-dan-fungsi-range)
4. [Perulangan `while`](#4-perulangan-while)
5. [Mengendalikan Loop: `break` dan `continue`](#5-mengendalikan-loop-break-dan-continue)
6. [Panduan Latihan Praktik](#6-panduan-latihan-praktik)
7. [🎓 Studi Kasus: Rekap Nilai Kuis Kelas](#7-studi-kasus-rekap-nilai-kuis-kelas)
8. [💡 Tips & Jebakan Umum dari Asprak](#8-tips--jebakan-umum-dari-asprak)

---

## 1. Percabangan Bertingkat (Nested If)
Percabangan bertingkat adalah struktur `if` yang berada di dalam blok `if`, `elif`, atau `else` lainnya. Kondisi di dalam (kondisi dalam) **hanya akan diperiksa jika kondisi di luar (kondisi luar) sudah terpenuhi (True)**.

### Kapan pakai `elif` vs Nested `if`?
| Aspek | `elif` (Sejajar) | `if` Bertingkat (Berlapis) |
| :--- | :--- | :--- |
| **Bentuk Keputusan** | Satu pilihan dari banyak kondisi yang saling lepas. | Keputusan tahap kedua bergantung pada hasil tahap pertama. |
| **Letak `if`** | Sejajar pada indentasi yang sama. | `if` di dalam blok `if` lain (indentasi lebih dalam). |
| **Contoh Kasus** | Konversi nilai (A/B/C/D). | Cek umur dulu, jika >= 17 baru cek status kartu pelajar. |

**Contoh Kode:**
```python
umur = int(input("Masukkan umur: "))
kartu_pelajar = input("Punya kartu pelajar? (ya/tidak): ")

if umur >= 17:
    print("Umur memenuhi syarat nonton film 17+")
    if kartu_pelajar == "ya":  # <-- Nested If (Indentasi lebih dalam)
        print("Tiket: harga pelajar Rp30000")
    else:
        print("Tiket: harga umum Rp45000")
else:
    print("Maaf, film ini khusus usia 17 tahun ke atas")
```

---

## 2. Konsep Dasar Perulangan (Looping)
Bayangkan Anda diminta mencetak angka 1 sampai 100. Menulis 100 baris `print()` sangat tidak efisien. Di sinilah **looping** berperan: menjalankan blok kode secara berulang.

Python memiliki dua jenis perulangan utama:
1. **`for`**: Digunakan ketika **jumlah pengulangan sudah diketahui**.
2. **`while`**: Digunakan ketika **jumlah pengulangan belum diketahui** (berhenti berdasarkan kondisi).

---

## 3. Perulangan `for` dan Fungsi `range()`
Perulangan `for` di Python biasanya dipasangkan dengan fungsi `range()` untuk menghasilkan urutan angka.

**Sintaks:**
```python
for variabel in range(awal, akhir, langkah):
    # blok kode yang diulang
```

### Variasi `range()`
| Penulisan | Urutan yang Dihasilkan | Keterangan |
| :--- | :--- | :--- |
| `range(5)` | 0, 1, 2, 3, 4 | Mulai dari 0, berhenti sebelum 5. |
| `range(1, 6)` | 1, 2, 3, 4, 5 | Mulai dari 1, berhenti sebelum 6. |
| `range(2, 11, 2)` | 2, 4, 6, 8, 10 | Mulai dari 2, langkah naik 2. |
| `range(5, 0, -1)` | 5, 4, 3, 2, 1 | Mulai dari 5, langkah mundur 1. |

> ⚠️ **Ingat:** Nilai `akhir` pada `range()` **tidak ikut** dihitung (exclusive).

---

## 4. Perulangan `while`
Perulangan `while` akan terus berjalan selama kondisinya bernilai `True`.

**Sintaks:**
```python
while kondisi:
    # blok kode yang diulang
    # PENTING: ubah variabel agar kondisi suatu saat menjadi False!
```

**Contoh:**
```python
total = 0
angka = int(input("Masukkan angka (0 untuk berhenti): "))

while angka != 0:
    total = total + angka
    angka = int(input("Masukkan angka (0 untuk berhenti): ")) # Update variabel!

print("Total semua angka:", total)
```

---

## 5. Mengendalikan Loop: `break` dan `continue`
Terkadang kita perlu memaksa loop berhenti atau melompati iterasi tertentu.

*   **`break`**: Menghentikan perulangan **seketika**. Program langsung keluar dari loop dan lanjut ke baris setelahnya.
*   **`continue`**: Melewati sisa kode pada iterasi saat ini, lalu **langsung lanjut ke iterasi berikutnya**.

**Contoh:**
```python
for i in range(1, 11):
    if i == 8:
        break       # Loop berhenti total saat i = 8
    if i % 2 == 0:
        continue    # Lewati angka genap, lanjut ke angka berikutnya
    print(i)
# Output: 1, 3, 5, 7
```

---

## 6. Panduan Latihan Praktik

Kerjakan file berikut secara berurutan di VS Code. **Ketik ulang kodenya (jangan copy-paste)** agar terbiasa dengan logika dan indentasi!

### 📝 Latihan 1: Percabangan Bertingkat (`latihan1.py`)
*   **Fokus:** Memahami `if` di dalam `if`.
*   **Tugas:** Buat program cek tiket bioskop berdasarkan umur dan status kartu pelajar.
*   **Cara Run:** `python latihan1.py`

### 📝 Latihan 2: Perulangan `for` (`latihan2.py`)
*   **Fokus:** Memahami `range()` dan mencetak urutan.
*   **Tugas:** Cetak angka 1-5, lalu buat tabel perkalian 3 (3x1 sampai 3x5).
*   **Cara Run:** `python latihan2.py`

### 📝 Latihan 3: Perulangan `while` (`latihan3.py`)
*   **Fokus:** Looping berbasis kondisi dan penjumlahan akumulatif.
*   **Tugas:** Minta input angka terus menerus, jumlahkan, dan berhenti jika user mengetik `0`.
*   **Cara Run:** `python latihan3.py`

### 📝 Latihan 4: `break` dan `continue` (`latihan4.py`)
*   **Fokus:** Mengontrol alur loop.
*   **Tugas:** Cetak bilangan ganjil dari 1-10, tapi paksa berhenti jika angka mencapai 8.
*   **Cara Run:** `python latihan4.py`

---

## 7. 🎓 Studi Kasus: Rekap Nilai Kuis Kelas

Seorang dosen ingin merekap nilai kuis. Program harus meminta jumlah mahasiswa, lalu meminta nilai tiap mahasiswa. Program harus **validasi input** (hanya terima 0-100) dan **mengelompokkan nilai**.

### 📋 Ketentuan Logika
1.  **Input:** Jumlah mahasiswa (`int`).
2.  **Validasi Nilai:** Gunakan `while` untuk meminta ulang jika nilai < 0 atau > 100.
3.  **Kategori Nilai (Gunakan Nested If):**
    *   `>= 85`: Lulus Sangat Baik
    *   `60 - 84`: Lulus
    *   `40 - 59`: Remedial
    *   `< 40`: Tidak Lulus
4.  **Rekap Akhir:** Hitung Rata-rata, Nilai Tertinggi, Jumlah Lulus, Remedial, dan Tidak Lulus.

### 🧠 Alur Logika (Pseudo-code)
```text
1. Siapkan variabel: total=0, lulus=0, remedial=0, tidak_lulus=0, tertinggi=0
2. Input jumlah_mahasiswa
3. FOR i dari 1 sampai jumlah_mahasiswa:
     a. Input nilai
     b. WHILE nilai < 0 ATAU nilai > 100:
          - Print "Nilai harus 0-100, coba lagi"
          - Input nilai ulang
     c. IF nilai >= 60:
          - IF nilai >= 85: kategori = "Lulus Sangat Baik", lulus += 1
          - ELSE: kategori = "Lulus", lulus += 1
        ELSE:
          - IF nilai >= 40: kategori = "Remedial", remedial += 1
          - ELSE: kategori = "Tidak Lulus", tidak_lulus += 1
     d. Tambahkan nilai ke total
     e. IF nilai > tertinggi: tertinggi = nilai
     f. Print Kategori
4. Hitung rata-rata = total / jumlah_mahasiswa
5. Print Rekap Akhir
```

---

## 8. 💡 Tips & Jebakan Umum dari Asprak

Sebagai asprak, ini adalah error yang paling sering saya temui di Modul 2. Hindari ya!

### 🚨 1. Infinite Loop (Program Macet/Tidak Berhenti)
*   **Penyebab:** Pada perulangan `while`, Anda lupa mengubah nilai variabel yang dicek di dalam blok loop.
*   **Solusi:** Pastikan ada baris yang mengupdate variabel (misal: `angka = int(input(...))` di dalam loop).
*   **Cara Menghentikan:** Tekan **`Ctrl + C`** di terminal untuk memaksa program berhenti.

### 🚨 2. Off-by-One Error pada `range()`
*   **Penyebab:** Mengira `range(1, 5)` akan menghasilkan 1, 2, 3, 4, **5**.
*   **Fakta:** `range()` selalu berhenti **sebelum** angka akhir. `range(1, 5)` hanya menghasilkan 1, 2, 3, 4.
*   **Solusi:** Jika ingin sampai 5, gunakan `range(1, 6)`.

### 🚨 3. `IndentationError` pada Nested If
*   **Penyebab:** Salah menaruh spasi. Python sangat ketat soal indentasi. `if` di dalam `if` harus memiliki spasi yang lebih banyak (biasanya 8 spasi atau 2 tab) dibanding `if` luarnya.
*   **Solusi:** Gunakan fitur *Indent Guides* di VS Code (garis vertikal tipis di sebelah kode) untuk melihat blok kode Anda.

### 🚨 4. Salah Logika `break` dan `continue`
*   **Ingat:** 
    *   `break` = **Keluar** dari ruangan (loop).
    *   `continue` = **Lompat** ke awal ruangan lagi (iterasi berikutnya), mengabaikan kode di bawahnya.

---

**Selamat mengerjakan! Logika perulangan adalah fondasi utama pemrograman. Jika Anda paham Modul 2, Modul-modul selanjutnya akan terasa jauh lebih mudah.** 

*Jika ada kendala, jangan ragu untuk bertanya saat sesi praktikum berlangsung.*

---
