n = int(input("Jumlah hari: "))
suhu = []

for i in range(n):
    s = float(input("Suhu hari ke-" + str(i + 1) + ": "))
    suhu.append(s)

total = 0
for s in suhu:
    total = total + s
rata = total / len(suhu)

di_atas = 0
for s in suhu:
    if s > rata:
        di_atas = di_atas + 1

print("Data suhu :", suhu)
print("Rata-rata :", round(rata, 2))
print("Hari di atas rata-rata:", di_atas)       