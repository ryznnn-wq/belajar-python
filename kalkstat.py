print("======= kalkulator statistik ======")

data = list(map(int, input("masukkan angka (pisah dengan spasi): ").split()))

def input_data(*args):
    return list(args)

hasil = input_data(*data)

def hitung_statistik(data):
    total = 0
    tertinggi = 0
    terrendah = data[0]
    for all in data:
        jumlah_data = int(all)
        total += jumlah_data
        if jumlah_data > tertinggi:
            tertinggi = jumlah_data
        elif jumlah_data < terrendah:
            terrendah = jumlah_data
    pembulatan = lambda total: round(total, 2)
    ratarata = pembulatan(total / len(data))
    return {
        "total": total,
        "tertinggi": tertinggi,
        "terrendah": terrendah,
        "ratarata": ratarata
    }


print("======= hasil stattistik ======")
print(f"data: {hasil}")
for key, value in hitung_statistik(data).items():
    print(f"{key}: {value}")