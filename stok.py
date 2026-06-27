barang = [
    {"barang": "kopi", "stok": 10, "harga": 5000},
    {"barang": "teh", "stok": 5, "harga": 3000},
    {"barang": "susu", "stok": 3, "harga": 8000},
    {"barang": "air", "stok": 20, "harga": 2000},
    {"barang": "jus", "stok": 7, "harga": 10000},
]

print("======daftar barang======")
for no, item in enumerate(barang):
    print(f"{no+1}. {item['barang']} - Rp.{item['harga']} (stok: {item['stok']})")

nama_barang = input("masukkan nama barang: ")
jumlah_barang = int(input("masukkan jumlah: "))

for all in barang:
    nm_barang = all['barang']
    harga = int(all['harga'])
    stok = int(all['stok'])
    if nama_barang == nm_barang:
        if jumlah_barang > stok:
            print(f"stok {nama_barang} tidak mencukupi, tersedia {all['stok']}")
        elif jumlah_barang <= stok:
            total_bayar = jumlah_barang * harga
            print(f"total bayar: {jumlah_barang} x {all['harga']} = {total_bayar}")