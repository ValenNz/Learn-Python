def cari_posisi(data, target):
    posisi = -1
    i = 0
    while i < len(data) and posisi == -1:
        if data[i] == target:
            posisi = i
        i = i + 1
    return posisi

buku = ["Laskar Pelangi", "Bumi", "Dilan", "Negeri 5 Menara", "Pulang"]
judul = input("Cari judul buku: ")
hasil = cari_posisi(buku, judul)

if hasil == -1:
    print("Buku", judul, "tidak tersedia")
else:
    print("Buku", judul, "ada di rak nomor", hasil + 1)