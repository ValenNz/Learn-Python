keranjang = []
print("Keranjang awal:", keranjang)

keranjang.append("roti")
keranjang.append("susu")
keranjang.append("telur")
print("Setelah append:", keranjang)

keranjang.insert(1, "keju")
print("Setelah insert:", keranjang)

keranjang[0] = "roti gandum"
print("Setelah diubah:", keranjang)

keranjang.remove("susu")
print("Setelah remove:", keranjang)

terakhir = keranjang.pop()
print("Diambil dengan pop:", terakhir)
print("Keranjang akhir :", keranjang)

print("Jumlah barang :", len(keranjang))