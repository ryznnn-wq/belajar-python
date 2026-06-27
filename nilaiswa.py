siswa = []

jumlah = int(input("jumlah siswa: "))

for i in range(jumlah):
    print(f"input siswa ke {i+1}"),
    nilai = {
        "nama": input("nama: "),
        "nilai": input("nilai: ")
    }
    siswa.append(nilai)

print("======hasil nilai kelas========")
for no, item in enumerate(siswa):
    print(f"{no+1}. {item['nama']} - {item['nilai']}")

total = 0
tertinggi = 0
terrendah = 100
nama_tertinggi = ""
nama_terrendah = ""

for all in siswa:
    nilai_siswa = int(all['nilai'])
    total += nilai_siswa
    if nilai_siswa > tertinggi:
        tertinggi = nilai_siswa
        nama_tertinggi = f"{all['nama']}"
    if nilai_siswa < terrendah:
        terrendah = nilai_siswa
        nama_terrendah = f"{all['nama']}"

ratarata = total / jumlah

print(f"nilai tertinggi: {nama_tertinggi} ({tertinggi})")
print(f"nilai terrendah: {nama_terrendah} ({terrendah})")
print(f"rata rata kelas: {ratarata:.2f}")