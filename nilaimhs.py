print("======kalkulator nilai mahasiswa=======")

nama = input("masukkan nama mahasiswa: ")
tugas = int(input("masukkan nilai tugas: "))
uts = int(input("masukkan nilai uts: "))
uas = int(input("masukkan nilai uas: "))

nilai_tugas = tugas * 0.30
nilai_uts = uts * 0.30
nilai_uas = uas * 0.40
nilai_akhir = int(nilai_tugas + nilai_uts + nilai_uas)


for i in range(1, nilai_akhir+1):
    print(i)

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 55:
    grade = "C"
elif nilai_akhir >= 40:
    grade = "D"
else:
    grade = "E"

print("=====hasil akhir======")
print(f"nama: {nama}")
print(f"nilai tugas: {tugas}")
print(f"nilai uts: {uts}")
print(f"nilai uas: {uas}")
print(f"nilai akhir: {nilai_akhir}")
print(f"grade: {grade}")
