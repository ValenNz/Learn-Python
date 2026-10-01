# 🐍 Modul Praktikum 1: Variabel, Tipe Data, dan Percabangan

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Sistem Informasi  
**Bahasa Pemrograman:** Python 3  

Selamat datang di sesi praktikum pertama! 🎉  
Repository/Modul ini dirancang untuk membantu Anda memahami fondasi utama pemrograman Python: bagaimana menyimpan data, mengenali jenis data, dan membuat program yang dapat "mengambil keputusan".

---

## 📑 Daftar Isi
1. [Konsep Variabel](#1-variabel)
2. [Tipe Data Dasar](#2-tipe-data)
3. [Interaksi dengan Pengguna (Input/Output)](#3-input-dari-pengguna)
4. [Struktur Kontrol Percabangan](#4-struktur-kontrol-percabangan-if-else)
5. [Panduan Latihan & Studi Kasus](#5-panduan-latihan-dan-studi-kasus)
6. [💡 Tips & Common Errors dari Asprak](#6-tips--common-errors-dari-asprak)

---

## 1. Variabel
Variabel adalah "wadah" atau nama yang digunakan untuk menyimpan nilai di dalam memori komputer, sehingga nilai tersebut bisa dipanggil dan diproses ulang.

### Aturan Penulisan Variabel di Python
- **Tanpa Deklarasi Tipe:** Python sangat dinamis. Anda tidak perlu menuliskan tipe data (seperti `int` atau `string` di bahasa lain). Cukup gunakan tanda sama dengan (`=`).
  ```python
  nama = "Rendra"
  umur = 20
  ```
- **Karakter yang Diizinkan:** Hanya boleh terdiri dari huruf, angka, dan *underscore* (`_`). **Harus** diawali dengan huruf atau `_`.
- **Case-Sensitive:** Python membedakan huruf besar dan kecil. `nilai` dan `Nilai` adalah dua variabel yang berbeda.
- **Best Practice (Gaya Penulisan):** Gunakan nama yang deskriptif dan ikuti gaya **`snake_case`** (huruf kecil semua, dipisah underscore).
  ✅ `total_nilai`, `tinggi_badan`  
  ❌ `tn`, `TotalNilai`, `tinggibadan`

---

## 2. Tipe Data
Setiap nilai memiliki tipe data yang menentukan operasi apa yang bisa dilakukan terhadapnya. Python tidak memiliki tipe data karakter (`char`) tunggal; satu huruf seperti `"A"` tetap dianggap sebagai teks (`str`).

| Tipe Data | Keterangan | Contoh Nilai |
| :--- | :--- | :--- |
| `int` | Bilangan bulat (tanpa desimal) | `20`, `-5`, `100` |
| `float` | Bilangan desimal/pecahan | `168.5`, `3.14` |
| `str` | Teks/String (diapit tanda kutip) | `"Rendra"`, `"Surabaya"` |
| `bool` | Nilai logika (Boolean) | `True`, `False` |

**Cek Tipe Data:** Gunakan fungsi bawaan `type()` untuk mengetahui tipe data suatu variabel.
```python
huruf = "A"
print(type(huruf))  # Output: <class 'str'>
```

---

## 3. Input dari Pengguna
Untuk membuat program interaktif, kita menggunakan fungsi `input()`. 

⚠️ **ATURAN EMAS:** Fungsi `input()` **SELALU** mengembalikan nilai bertipe `str` (teks), meskipun pengguna mengetik angka. Jika Anda ingin melakukan operasi matematika, Anda **wajib** mengubahnya (konversi/casting) menggunakan `int()` atau `float()`.

```python
# Contoh yang BENAR
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: ")) # Konversi str ke int

print("Tahun depan usiamu", umur + 1, "tahun")
```

---

## 4. Struktur Kontrol Percabangan (if-else)
Percabangan memungkinkan program mengambil keputusan: menjalankan blok kode tertentu jika kondisi bernilai `True`, dan blok lain jika `False`.

### Kata Kunci: `if`, `elif`, `else`
Berbeda dengan bahasa lain yang menggunakan kurung kurawal `{}`, **Python menggunakan INDENTASI (spasi di awal baris)** untuk menandai blok kode.

```python
if kondisi:
    # Kode ini jalan jika kondisi True
elif kondisi_lain:
    # Kode ini jalan jika kondisi_lain True
else:
    # Kode ini jalan jika semua kondisi di atas False
```

### Operator Perbandingan
Gunakan operator ini untuk membangun kondisi: `==` (sama dengan), `!=` (tidak sama dengan), `>`, `<`, `>=`, `<=`.

### Operator Modulo (`%`)
Sangat berguna untuk mencari **sisa bagi**. Sering digunakan untuk mengecek bilangan Genap/Ganjil.
```python
angka = 7
if angka % 2 == 0:  # Jika sisa bagi dengan 2 adalah 0
    print("Genap")
else:
    print("Ganjil")
```

---

## 5. Panduan Latihan dan Studi Kasus

Kerjakan file berikut secara berurutan di VS Code. **Ketik ulang kode secara manual** (jangan *copy-paste*) agar terbiasa dengan sintaks Python!

### 📝 Latihan 1: Deklarasi & Tipe Data (`latihan1.py`)
Fokus: Memahami cara membuat variabel dan mengecek tipe datanya.
*(Lihat detail kode di modul PDF halaman 3)*

### 📝 Latihan 2: Input Pengguna (`latihan2.py`)
Fokus: Menggabungkan `input()`, konversi tipe data `int()`, dan operasi penjumlahan.

### 📝 Latihan 3: Percabangan Dasar (`latihan3.py`)
Fokus: Menggunakan `if-else` dan operator modulo `%` untuk cek Genap/Ganjil.

### 📝 Latihan 4: Percabangan Bertingkat (`latihan4.py`)
Fokus: Menggunakan `if-elif-else` untuk menentukan kategori nilai (A/B/C/D) berdasarkan rentang angka.
```python
if nilai >= 85:
    kategori = "A"
elif nilai >= 70:
    kategori = "B"
# ... dst
```

### 🎓 Studi Kasus: Cek Kelulusan (`studi_kasus.py`)
**Tugas:** Buat program yang meminta **Nama** dan **Nilai Akhir (0-100)**.
**Aturan Kelulusan:**
- Nilai >= 60 ➡️ **LULUS**
- Nilai < 60 ➡️ **TIDAK LULUS**

**Tantangan Tambahan (Opsional):** Gabungkan logika Latihan 4 ke dalam studi kasus ini, sehingga output tidak hanya menampilkan status Lulus/Tidak Lulus, tetapi juga Grade (A/B/C/D) mahasiswa!

---

## 6. 💡 Tips & Common Errors dari Asprak

Sebagai asprak, saya sering melihat mahasiswa melakukan kesalahan umum berikut. Hindari hal-hal ini ya!

1. **`IndentationError: expected an indented block`**
   - **Penyebab:** Anda lupa memberikan spasi (indentasi) setelah `if`, `elif`, atau `else`.
   - **Solusi:** Gunakan konsisten 4 spasi atau 1 tab untuk setiap blok di dalam percabangan.
2. **`TypeError: can only concatenate str (not "int") to str`**
   - **Penyebab:** Lupa mengonversi `input()` menjadi `int()` atau `float()` saat ingin melakukan perhitungan matematika.
   - **Solusi:** Bungkus input dengan `int()`, contoh: `int(input("..."))`.
3. **`SyntaxError: invalid syntax`**
   - **Penyebab:** Seringkali karena lupa tanda titik dua (`:`) di akhir baris `if`, `elif`, atau `else`.
   - **Solusi:** Pastikan selalu menulis `if kondisi:` (jangan lupa `:`).
4. **Salah Menggunakan Operator Sama Dengan**
   - `=` digunakan untuk **mengisi nilai** ke variabel (Assignment).
   - `==` digunakan untuk **membandingkan** dua nilai di dalam `if`.

---

**Selamat belajar dan selamat ngoding! Jika ada kendala, jangan ragu untuk bertanya saat sesi praktikum berlangsung.** 🚀