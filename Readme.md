# 🐍 Repository Praktikum Algoritma & Pemrograman (Python)

**Mata Kuliah:** Algoritma dan Pemrograman  
**Program Studi:** S1 Sistem Informasi  
**Bahasa Pemrograman:** Python 3  
**Asisten Praktikum:** Nuevalen Refitra Alswando 

Selamat datang di repository praktikum Alpro! 🎉  
Repository ini berisi seluruh materi, latihan, dan studi kasus untuk setiap modul praktikum. README ini akan memandu Anda dari **setup awal** hingga **cara menjalankan kode** dan **troubleshooting** umum.

---

##  Daftar Isi
1. [Persiapan & Setup](#1-persiapan--setup)
2. [Cara Menjalankan Program Python](#2-cara-menjalankan-program-python)
3. [Shortcuts VS Code yang Wajib Diketahui](#3-shortcuts-vs-code-yang-wajib-diketahui)
4. [Struktur Repository](#4-struktur-repository)
5. [Modul 01 — Variabel, Tipe Data, dan Percabangan](#5-modul-01--variabel-tipe-data-dan-percabangan)
6. [Modul 02 — Coming Soon](#6-modul-02--coming-soon)
7. [Common Errors & Troubleshooting](#7-common-errors--troubleshooting)
8. [💡 Tips dari Asprak](#8-tips-dari-asprak)

---

## 1. Persiapan & Setup

Sebelum mulai coding, pastikan Anda sudah menginstal:

### ✅ Python 3
- Download dari [python.org](https://www.python.org/downloads/)
- **PENTING:** Saat instalasi, **centang** opsi *"Add Python to PATH"*
- Cek instalasi dengan membuka terminal dan ketik:
  ```bash
  python --version
  # atau
  python3 --version
  ```

### ✅ Visual Studio Code (VS Code)
- Download dari [code.visualstudio.com](https://code.visualstudio.com/)
- Instal ekstensi **Python** dari Microsoft (cari di Extensions marketplace)

### ✅ Git (Opsional tapi direkomendasikan)
- Untuk clone repository ini: [git-scm.com](https://git-scm.com/)

---

## 2. Cara Menjalankan Program Python

### 🖥️ Melalui Terminal VS Code (Paling Direkomendasikan)

**Langkah 1: Buka Terminal**
- Tekan **`Ctrl + ~`** (tilde) atau **`Ctrl + J`** untuk toggle terminal panel
- Atau via menu: **Terminal → New Terminal**

**Langkah 2: Pindah ke folder modul**
```bash
cd modul01
```

**Langkah 3: Jalankan file Python**
```bash
python namafile.py
# atau jika menggunakan python3
python3 namafile.py
```

**Contoh:**
```bash
cd modul01
python latihan1.py
```

### ️ Melalui Tombol Run di VS Code
- Buka file `.py`
- Klik tombol **▶️ Run** di pojok kanan atas editor
- Atau klik kanan di editor → **Run Python File in Terminal**

### ⌨️ Melalui Command Prompt / PowerShell (Windows)
```cmd
cd C:\path\ke\Alpro\modul01
python latihan1.py
```

### 🐧 Melalui Terminal (Linux/Mac)
```bash
cd ~/path/ke/Alpro/modul01
python3 latihan1.py
```

---

## 3. Shortcuts VS Code yang Wajib Diketahui

| Shortcut | Fungsi |
|----------|--------|
| `Ctrl + ~` atau `Ctrl + J` | Buka/tutup terminal |
| `Ctrl + Shift + P` | Buka Command Palette (cari command apa saja) |
| `Ctrl + N` | Buat file baru |
| `Ctrl + S` | Simpan file |
| `Ctrl + \` | Split editor (buka 2 file berdampingan) |
| `Ctrl + P` | Quick open file (cari file cepat) |
| `Ctrl + /` | Comment/uncomment kode |
| `Ctrl + Z` | Undo |
| `Ctrl + Shift + Z` | Redo |
| `F5` | Run & Debug |
| `Ctrl + F` | Find dalam file |
| `Ctrl + Shift + F` | Find di seluruh folder |
| `Alt + ↑/↓` | Pindahkan baris kode ke atas/bawah |
| `Shift + Alt + ↑/↓` | Copy baris ke atas/bawah |
| `Ctrl + D` | Select kata yang sama berikutnya |

---

## 4. Struktur Repository

```
Alpro/
├── Readme.md              ← Panduan universal ini
├── modul01/
│   ├── Readme.md          ← Panduan spesifik Modul 1
│   ├── Modul Praktikum 1.pdf
│   ├── latihan1.py        ← Deklarasi Variabel & Tipe Data
│   ├── latihan2.py        ← Input dari Pengguna
│   ├── latihan3.py        ← Percabangan if-else
│   ├── latihan4.py        ← Percabangan if-elif-else
│   ── studi_kasus.py     ← Program Cek Kelulusan
├── modul02/
│   └── Readme.md          ← (Coming Soon)
└── ...
```

---

## 5. Modul 01 — Variabel, Tipe Data, dan Percabangan

###  Tujuan Pembelajaran
- Memahami konsep variabel dan aturan penamaannya
- Mengenal tipe data dasar Python (`int`, `float`, `str`, `bool`)
- Menggunakan `input()` dan konversi tipe data
- Membuat keputusan program dengan `if`, `elif`, `else`

### 📋 Daftar Latihan

| File | Topik | Cara Run |
|------|-------|----------|
| `latihan1.py` | Deklarasi Variabel & Tipe Data | `python latihan1.py` |
| `latihan2.py` | Input dari Pengguna | `python latihan2.py` |
| `latihan3.py` | Percabangan if-else (Genap/Ganjil) | `python latihan3.py` |
| `latihan4.py` | Percabangan if-elif-else (Kategori Nilai) | `python latihan4.py` |
| `studi_kasus.py` | Program Cek Kelulusan | `python studi_kasus.py` |

### 📖 Ringkasan Materi

#### Variabel
```python
nama = "Aurora"        # str
umur = 21              # int
tinggi_badan = 165.0   # float
adalah_mahasiswa = True  # bool
```

#### Input & Konversi Tipe Data
```python
nama = input("Masukkan nama: ")        # Selalu str
umur = int(input("Masukkan umur: "))   # Konversi ke int
tinggi = float(input("Tinggi: "))      # Konversi ke float
```

#### Percabangan
```python
if kondisi:
    # blok kode jika True
elif kondisi_lain:
    # blok kode jika kondisi_lain True
else:
    # blok kode jika semua False
```

### 🎓 Studi Kasus: Cek Kelulusan
Buat program yang meminta nama dan nilai akhir, lalu tampilkan status kelulusan (≥60 = Lulus, <60 = Tidak Lulus).

**Contoh output:**
```
Masukkan nama mahasiswa: Charles Xavier
Masukkan nilai akhir: 72
Charles Xavier dengan nilai akhir 72 dinyatakan LULUS
```

---

## 6. Modul 02 — Coming Soon

*Materi Modul 2 akan ditambahkan segera. Stay tuned!* 🚀

---

## 7. Common Errors & Troubleshooting

### ❌ `IndentationError: expected an indented block`
**Penyebab:** Lupa memberi spasi/indentasi setelah `if`, `elif`, `else`, `def`, `for`, `while`.  
**Solusi:** Tekan `Tab` atau 4 spasi untuk blok kode di dalam struktur kontrol.

### ❌ `SyntaxError: invalid syntax`
**Penyebab:** Seringkali karena lupa tanda titik dua (`:`) di akhir baris `if`, `elif`, `else`.  
**Solusi:** Pastikan selalu menulis `if kondisi:` (jangan lupa `:`).

### ❌ `TypeError: can only concatenate str (not "int") to str`
**Penyebab:** Lupa mengonversi `input()` menjadi `int()` atau `float()`.  
**Solusi:** Bungkus input dengan `int()` atau `float()`:
```python
umur = int(input("Masukkan umur: "))
```

### ❌ `NameError: name 'x' is not defined`
**Penyebab:** Menggunakan variabel yang belum dideklarasikan, atau salah ketik nama variabel.  
**Solusi:** Cek penamaan variabel (ingat: Python **case-sensitive**).

### ❌ `ValueError: invalid literal for int() with base 10`
**Penyebab:** Mencoba mengonversi teks (bukan angka) menjadi `int()`.  
**Solusi:** Pastikan input yang dimasukkan adalah angka, atau gunakan `try-except` untuk handling error.

### ❌ `python is not recognized as an internal or external command`
**Penyebab:** Python belum ditambahkan ke PATH saat instalasi.  
**Solusi:** 
- Reinstall Python dan centang "Add Python to PATH"
- Atau gunakan `py` atau `python3` sebagai gantinya

---

## 8. 💡 Tips dari Asprak

1. **Ketik Ulang, Jangan Copy-Paste!**  
   Mengetik kode manual akan melatih muscle memory dan membuat Anda lebih familiar dengan sintaks Python.

2. **Gunakan Nama Variabel yang Deskriptif**  
   ✅ `total_nilai`, `tinggi_badan`  
   ❌ `tn`, `x`, `abc`, `TotalNilai`

3. **Selalu Simpan File Sebelum Run**  
   Tekan `Ctrl + S` sebelum menjalankan kode. VS Code kadang tidak otomatis menyimpan.

4. **Baca Error Message dengan Teliti**  
   Python biasanya memberi tahu **baris berapa** error terjadi. Perhatikan nomor baris di terminal.

5. **Gunakan `print()` untuk Debugging**  
   Jika program tidak berjalan sesuai harapan, tambahkan `print()` di tengah kode untuk melihat nilai variabel.

6. **Komentar itu Penting**  
   Gunakan `#` untuk memberi catatan pada kode yang kompleks:
   ```python
   # Cek apakah angka genap atau ganjil
   if angka % 2 == 0:
       print("Genap")
   ```

7. **Eksperimen!**  
   Jangan takut mengubah kode dan melihat apa yang terjadi. Belajar coding = banyak trial & error.

8. **Jangan Malu Bertanya**  
   Jika stuck lebih dari 15 menit, tanya asprak atau teman. Jangan habiskan waktu 1 jam hanya untuk satu error kecil.

---

## 📚 Referensi Tambahan

- [Dokumentasi Resmi Python](https://docs.python.org/3/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

---

**Selamat belajar dan selamat ngoding! **  
*Jika ada kendala, jangan ragu untuk bertanya saat sesi praktikum berlangsung.*

---

*Last updated: Oktober 2026*  
*Maintained by: Nuevalen Refitra Alswando - Asisten Praktikum Alpro*