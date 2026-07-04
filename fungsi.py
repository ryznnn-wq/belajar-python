print("======kalkulator geometri======")
print("1. persegi \n2. lingkaran \n3. segitiga")

def luaspersegi(sisi):
    luas = sisi * sisi
    return luas

def luaslingkaran(jarijari):
    luas = 3.14 * jarijari * jarijari
    return luas

def luassegitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

pilihan = int(input("pilih bentuk: "))

if pilihan == 1:
    sisi = int(input("masukkan sisi: "))
    hitung = luaspersegi(sisi)
    print(f"luas persegi: {hitung}")
elif pilihan == 2:
    jarijari = int(input("masukkan jarijari: "))
    hitung = luaslingkaran(jarijari)
    print(f"luas lingkaran: {hitung}")
elif pilihan == 3: 
    alas = int(input("masukkan alas: "))
    tinggi = int(input("masukkan tinggi: "))
    hitung = luassegitiga(alas, tinggi)
    print(f"luas segitiga: {hitung}")