class mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def perkenalan(self):
        print(f"halo, nama saya {self.nama}, nim {self.nim}, jurusan saya {self.jurusan}")

    def info(self):
        daftar = {
            "nama": self.nama,
            "nim": self.nim,
            "jurusan": self.jurusan
        }
        return daftar

        
mhs1 = mahasiswa("dayat", 12345, "ilkom")
mhs2 = mahasiswa("sari", 23455, "ilkom")


mhs1.perkenalan()
mhs2.perkenalan()

print(mhs1.info())
print(mhs2.info())
