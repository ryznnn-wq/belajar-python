print("=======input biodata======")

data = {
    "nama": input("nama: "),
    "umur": input("umur: "),
    "jurusan": input("jurusan: "),
    "asal": input("asal kota: ")
}

print("========biodata=======")
for key, value in data.items():
    print(f"{key}: {value}")


# print(f"nama: {data['nama']}")
# print(f"umur: {data['umur']} tahun")
# print(f"jurusan: {data['jurusan']}")
# print(f"asal: {data['asal']}")
