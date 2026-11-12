# 🔄 Modul Praktikum 9: Fungsi, Parameter, dan Nilai Kembalian

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Sistem Informasi  
**Bahasa Pemrograman:** Python 3  
**Asisten Praktikum:** [Nama Anda]  

Selamat datang di sesi praktikum kesembilan! 🎉  
Di modul-modul sebelumnya, kode kita semakin panjang dan mulai terasa berantakan. Di Modul 9 ini, kita akan belajar merapikan program dengan **Fungsi (Function)**. Fungsi ibarat "mesin" kecil yang memiliki satu tugas spesifik, bisa kita pakai berulang kali, dan membuat kode kita jauh lebih mudah dibaca dan di-debug.

> ⚠️ **Catatan:** Untuk panduan instalasi Python, cara membuka terminal, dan shortcut VS Code, silakan baca **[README Universal di root folder](../Readme.md)**.

---

## 📑 Daftar Isi
1. [Pengertian & Anatomi Fungsi](#1-pengertian--anatomi-fungsi)
2. [Parameter vs Argumen & `return` vs `print`](#2-parameter-vs-argumen--return-vs-print)
3. [Lingkup Variabel (Scope)](#3-lingkup-variabel-scope)
4. [Modul Bawaan: `math` dan `random`](#4-modul-bawaan-math-dan-random)
5. [Pengenalan Rekursi](#5-pengenalan-rekursi)
6. [Panduan Latihan Praktik](#6-panduan-latihan-praktik)
7. [🎓 Studi Kasus: Kalkulator Nilai Akhir Mahasiswa](#7-studi-kasus-kalkulator-nilai-akhir-mahasiswa)
8. [💡 Tips & Jebakan Umum dari Asprak](#8-tips--jebakan-umum-dari-asprak)

---

## 1. Pengertian & Anatomi Fungsi
Fungsi adalah sekumpulan perintah yang diberi nama dan dapat dipanggil berkali-kali. Dengan fungsi, program yang panjang dipecah menjadi bagian-bagian kecil.

**Manfaat:** Kode tidak perlu ditulis berulang, mudah dibaca, bisa diuji terpisah, dan perubahan aturan cukup dilakukan di satu tempat.

**Anatomi Fungsi:**
```python
def hitung_luas(panjang, lebar):  # <-- Header fungsi (def, nama, parameter)
    luas = panjang * lebar         # <-- Badan fungsi (harus menjorok/indent)
    return luas                    # <-- Nilai kembalian

hasil = hitung_luas(4, 3)          # <-- Memanggil fungsi
print(hasil)
```
> ⚠️ **Aturan Emas:** Fungsi **harus didefinisikan** (ditulis kode `def`-nya) **sebelum** dipanggil di baris kode manapun.

---

## 2. Parameter vs Argumen & `return` vs `print`
Ini adalah konsep paling krusial di modul ini. Mari kita bedah satu per satu.

### Parameter vs Argumen
| Istilah | Pengertian | Contoh pada `hitung_luas` |
| :--- | :--- | :--- |
| **Parameter** | Variabel penampung yang ditulis di *header* fungsi. | `panjang`, `lebar` |
| **Argumen** | Nilai nyata yang dikirim saat fungsi *dipanggil*. | `4`, `3` |

### `return` vs `print`
Banyak pemula tertukar di sini! `print` hanya untuk menampilkan teks ke layar (untuk manusia), sedangkan `return` untuk mengirim nilai kembali ke program (untuk komputer diproses lagi).

| Aspek | `print` | `return` |
| :--- | :--- | :--- |
| **Fungsi** | Menampilkan nilai ke layar | Mengirim nilai kembali ke pemanggil |
| **Hasil disimpan di variabel?** | ❌ Tidak (variabel jadi `None`) | ✅ Ya |
| **Hasil bisa dihitung lagi?** | ❌ Tidak | ✅ Ya |
| **Ditujukan untuk** | Manusia yang membaca layar | Program yang memakai hasilnya |

**Contoh Perbedaan:**
```python
def luas_cetak(p, l): print(p * l)
def luas_hitung(p, l): return p * l

a = luas_cetak(3, 4)   # Layar: 12 | Variabel 'a' isinya None
b = luas_hitung(3, 4)  # Layar: Kosong | Variabel 'b' isinya 12
print(b + 10)          # Bisa dihitung lagi! Output: 22
```

---

## 3. Lingkup Variabel (Scope)
*   **Variabel Lokal:** Dibuat di *dalam* fungsi. Hanya ada saat fungsi berjalan dan **tidak bisa** diakses dari luar.
*   **Variabel Global:** Dibuat di *luar* semua fungsi. Bisa dibaca dari dalam fungsi.

```python
bonus = 10  # <-- Global
def tambah_bonus(nilai):
    hasil = nilai + bonus  # <-- 'hasil' adalah Lokal
    return hasil

print(tambah_bonus(80))    # Output: 90
# print(hasil)             # ❌ ERROR! NameError karena 'hasil' itu lokal.
```
> 💡 **Best Practice:** Kirim data ke fungsi melalui *parameter*, dan ambil hasilnya melalui *return*. Hindari mengandalkan variabel global di dalam fungsi.

---

## 4. Modul Bawaan: `math` dan `random`
Python punya banyak fungsi siap pakai di dalam "modul". Kita harus memuatnya dengan `import`.

```python
import math
import random

# Modul math
print(math.sqrt(16))       # 4.0 (Akar kuadrat)
print(math.ceil(4.2))      # 5 (Pembulatan ke atas)
print(math.floor(4.8))     # 4 (Pembulatan ke bawah)
print(math.pi)             # 3.14159...

# Modul random
print(random.randint(1, 6)) # Bilangan bulat acak 1 sampai 6
print(random.random())      # Desimal acak antara 0 sampai < 1
```

---

## 5. Pengenalan Rekursi
Rekursi adalah fungsi yang **memanggil dirinya sendiri**. Setiap fungsi rekursif **WAJIB** memiliki dua bagian:
1.  **Base Case:** Kondisi berhenti (jawaban langsung diketahui).
2.  **Recursive Case:** Memanggil diri sendiri dengan masalah yang lebih kecil.

```python
def faktorial(n):
    if n == 0:               # <-- Base Case
        return 1
    return n * faktorial(n-1) # <-- Recursive Case

print(faktorial(4)) # Output: 24 (4 * 3 * 2 * 1)
```
> 🚨 **Bahaya:** Jika tidak ada *Base Case*, fungsi akan memanggil dirinya terus-menerus sampai Python menyerah (`RecursionError`).

---

## 6. Panduan Latihan Praktik

Kerjakan file berikut secara berurutan. **Ketik ulang kodenya** agar terbiasa dengan sintaks fungsi!

### 📝 Latihan 1: Fungsi Tanpa Nilai Kembalian (`latihan1.py`)
*   **Fokus:** Membuat prosedur (fungsi void) dan fungsi yang memanggil fungsi lain.
*   **Tugas:** Buat fungsi `cetak_garis` dan `kartu_nama`.
*   **Cara Run:** `python latihan1.py`

### 📝 Latihan 2: Fungsi dengan `return` (`latihan2.py`)
*   **Fokus:** Mengembalikan nilai dan memanipulasinya di luar fungsi.
*   **Tugas:** Konversi suhu dan menghitung total luas ruangan.
*   **Cara Run:** `python latihan2.py`

### 📝 Latihan 3: `return` di Dalam Percabangan (`latihan3.py`)
*   **Fokus:** Mengembalikan nilai boolean (`True`/`False`) untuk validasi.
*   **Tugas:** Buat fungsi `lulus(nilai)` yang mengembalikan boolean, lalu pakai di `if`.
*   **Cara Run:** `python latihan3.py`

### 📝 Latihan 4: Modul `math` dan `random` (`latihan4.py`)
*   **Fokus:** Mengintegrasikan modul bawaan ke dalam fungsi buatan sendiri.
*   **Tugas:** Hitung jarak dua titik dan simulasi lempar dadu.
*   **Cara Run:** `python latihan4.py`

### 📝 Latihan 5: Pengenalan Rekursi (`latihan5.py`)
*   **Fokus:** Memahami *Base Case* dan *Recursive Case*.
*   **Tugas:** Buat fungsi faktorial dan hitung mundur rekursif.
*   **Cara Run:** `python latihan5.py`

---

## 7. 🎓 Studi Kasus: Kalkulator Nilai Akhir Mahasiswa

Seorang dosen ingin menghitung nilai akhir beberapa mahasiswa. Program harus meminta input nilai (Tugas, UTS, UAS), **memvalidasi** agar nilainya 0-100, menghitung Nilai Akhir (NA), menentukan Nilai Huruf, dan merekap jumlah yang lulus.

### 📋 Ketentuan Perhitungan
| Komponen | Bobot |
| :--- | :--- |
| Tugas | 30% |
| UTS | 30% |
| UAS | 40% |

| Nilai Akhir (NA) | Nilai Huruf | Status |
| :--- | :--- | :--- |
| NA ≥ 85 | A | Lulus |
| 70 ≤ NA < 85 | B | Lulus |
| 55 ≤ NA < 70 | C | Lulus |
| NA < 55 | D | Tidak Lulus |

### 🛠️ Fungsi yang Wajib Dibuat
1.  `nilai_valid(n)` -> Mengembalikan `True` jika 0 ≤ n ≤ 100.
2.  `baca_nilai(label)` -> Membaca input, mengulang pakai `while` jika tidak valid.
3.  `nilai_akhir(tugas, uts, uas)` -> Mengembalikan NA.
4.  `nilai_huruf(na)` -> Mengembalikan "A", "B", "C", atau "D".

### 🧠 Alur Logika (Pseudo-code)
```text
1. DEF nilai_valid(n): RETURN 0 <= n <= 100
2. DEF baca_nilai(label):
     WHILE TRUE:
       nilai = float(input(label))
       IF nilai_valid(nilai): RETURN nilai
       ELSE: PRINT "Nilai harus 0 sampai 100."
3. DEF nilai_akhir(t, u1, u2): RETURN (t*0.3) + (u1*0.3) + (u2*0.4)
4. DEF nilai_huruf(na):
     IF na >= 85: RETURN "A"
     ELIF na >= 70: RETURN "B"
     ... (dst)
5. PROGRAM UTAMA:
     jumlah_mhs = int(input("Jumlah mahasiswa: "))
     total_lulus = 0
     FOR i dari 1 sampai jumlah_mhs:
       nama = input("Nama: ")
       t = baca_nilai("Nilai tugas: ")
       u1 = baca_nilai("Nilai UTS: ")
       u2 = baca_nilai("Nilai UAS: ")
       
       na = nilai_akhir(t, u1, u2)
       huruf = nilai_huruf(na)
       
       PRINT f"{nama} -> NA: {round(na, 2)} | Huruf: {huruf}"
       IF na >= 55: total_lulus += 1
       
     PRINT f"Jumlah lulus: {total_lulus} dari {jumlah_mhs}"
