siswa = []

def tambah_siswa(siswa, nama, nilai):
    data = {"nama": nama, "nilai": nilai}
    siswa.append(data)

def tampil_siswa(siswa):
    for no, item in enumerate(siswa):
        print(f"{no+1}. {item['nama']} - {item['nilai']}")

def cari_siswa(siswa, nama):
    for item in siswa:
        if item['nama'] == nama:
            return item

def ratarata(siswa):
    total = 0
    for item in siswa:
        total += item['nilai']
    return total / len(siswa)

while True:
    print("======manajemen nilai siswa=====")
    print("1. tambah siswa\n2. tampilkan semua siswa\n3. cari siswa\n4. rata-rata nilai\n5. keluar")
    pilihan = int(input("pilih menu: "))

    if pilihan == 1:
        nama = input("nama: ")
        nilai = int(input("nilai: "))
        tambah_siswa(siswa, nama, nilai)
        print("siswa berhasil ditambahkan")
    elif pilihan == 2:
        tampil_siswa(siswa)
    elif pilihan == 3:
        nama = input("cari nama: ")
        hasil = cari_siswa(siswa, nama)
        if hasil:
            print(f"nama: {hasil['nama']}")
            print(f"nilai: {hasil['nilai']}")
        else:
            print("siswa tidak ditemukan")
    elif pilihan == 4:
        print(f"rata-rata nilai: {ratarata(siswa)}")
    elif pilihan == 5:
        break