mapel = ["Alpro", "Matdis", "PTI", "Bahasa Inggris", "Agama"]

print("Mata kuliah pertama:", mapel[0])
print("Mata kuliah terakhir:", mapel[-1])
print("Jumlah mata kuliah :", len(mapel))

print("Tiga pertama :", mapel[0:3])
print("Dua terakhir :", mapel[-2:])

if "Alpro" in mapel:
    print("Alpro ada di jadwal semester ini")