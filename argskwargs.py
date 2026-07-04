def jumlah(*args):
    total = 0
    for angka in args:
       total += angka
    return total

def tampilkan_profil(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("======args dan kwargs========")
while True:
    pilihan = int(input("pilih 1/2 (3 untuk keluar): "))
    if pilihan == 1:
        print(jumlah(10, 20, 30))
        print(jumlah(5, 10))
        print(jumlah(1, 2, 3, 4, 5))
    elif pilihan == 2:
        print("====== profil ====")
        tampilkan_profil(nama = "dayat", umur = 19, hobi="tidur")
    elif pilihan == 3:
        break