nama = input("masukkan nama: ")
nilai = int(input("masukkan nilai anda: "))

if nilai >= 90:
    print(f"halo {nama}, selamat nilai anda {nilai}, nilai anda A")
elif nilai >= 75:
    print(f"halo {nama}, selamat nilai anda {nilai}, nilai anda B")
elif nilai >= 60:
    print(f"halo {nama}, selamat nilai anda {nilai}, nilai anda C")
elif nilai >= 50:
    print(f"halo {nama}, selamat nilai anda {nilai}, nilai anda D belajar lagi yaa")
else:
    print(f"halo {nama}, nilai anda {nilai}, nilai anda E anda tidak lulus")