barang = []

for i in range(1, 6):
    barang.append(input("masukkan nama barang: "))

for a, i in enumerate(barang):
    print(f"{a+1}. {barang[a]}")