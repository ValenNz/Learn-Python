def min_maks(data):
    terkecil = data[0]
    terbesar = data[0]
    
    for x in data:
        if x < terkecil:
            terkecil = x
        if x > terbesar:
            terbesar = x
            
    return (terkecil, terbesar)

hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")
langkah = [4500, 8200, 3900, 10100, 7600]

kecil, besar = min_maks(langkah)
print("Langkah paling sedikit:", kecil)
print("Langkah paling banyak:", besar)

for i in range(len(hari)):
    print(hari[i], ":", langkah[i], "langkah")