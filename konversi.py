print("====== konversi satuan =====")
inputkm = int(input("Masukkan km: "))
inputkg = int(input("masukkan kg: "))
inputc = int(input("masukkan celcius: "))
print("\n")

pembulatan = lambda angka: round(angka, 2)


def laporan_konversi(*hasil):
    for no, item in enumerate(hasil):
        print(f"{no+1}. {item}")

def km_ke_mil(km):
    return km * 0.621371

def kg_ke_pon(kg):
    return kg * 2.20462

def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

print("===== hasil konversi ====")
print(f"1. {inputkm} km = {pembulatan(km_ke_mil(inputkm))} mil")
print(f"2. {inputkg} kg = {pembulatan(kg_ke_pon(inputkg))} pon")
print(f"3. {inputc} celcius= {pembulatan(celcius_ke_fahrenheit(inputc))} fahrenheit \n")


print("===== laporan konversi ======")
konversi = laporan_konversi("konversi km selesai", "konversi kg selesai", "konversi celcius selesai")
