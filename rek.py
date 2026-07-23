class RekeningBank:
    def __init__(self, nama_pemilik):
        self.nama_pemilik = nama_pemilik
        self.saldo = 0

    def setor(self, jumlah):
        self.saldo = self.saldo + jumlah
        print(f"setor: {jumlah} -> saldo: {self.saldo}")

    def tarik(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo = self.saldo - jumlah
            print(f"tarik: {jumlah} -> saldo: {self.saldo}")
        elif self.saldo <= jumlah:
            print(f"tarik: {jumlah} -> gagal! saldo tidak cukup. saldo: {self.saldo}")

    def cek_saldo(self):
        print(f"saldo anda: {self.saldo}")

rekening = RekeningBank("dayat")

rekening.setor(500000)
rekening.setor(200000)
rekening.tarik(300000)
rekening.tarik(500000)
rekening.cek_saldo()
