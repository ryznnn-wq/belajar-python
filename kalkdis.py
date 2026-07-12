def laporan(*produk):
    for no, item in enumerate(produk):
        print(f"{no+1}. {item}")

print("===== produk dalam toko =====")
produk = laporan("sepatu", "baju", "celana", "topi")

format_rupiah = lambda angka: f"Rp.  {angka:,}".replace(",", ".")
nama_produk = input("nama produk: ")
harga_awal = int(input(f"harga awal: "))
diskon = int(input("diskon: "))

def kategori_diskon(persen):
    if persen >= 50:
        persen = "diskon gila"
    elif persen >= 40:
        persen = "diskon besar"
    elif persen >= 30:
        persen = "diskon lumayan"
    elif persen >= 10:
        persen = "diskon kecil"
    return persen

def hitung_diskon(harga, persen_diskon):
    harga_akhir = harga - (harga * persen_diskon / 100)
    return int(harga_akhir)

print("====== kalkulator diskon toko =====")
print(f"nama produk: {nama_produk}")
print(f"harga awal: {format_rupiah(harga_awal)}")
print(f"diskon: {diskon}%")
print(f"harga akhir: {format_rupiah(hitung_diskon(harga_awal, diskon))}")
print(f"kategori: {kategori_diskon(diskon)}")