#class = cetakan blueprint
#object = hasil dari desain
# def __init__ = construktor
class Barista:
    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji
        self.pesanan_diantar = []

    def ambil_pesanan(self, pesanan):
        print(f"{self.nama} mengamibil pesanan dari pelanggan, info pesanan : {pesanan}")

    def antar_pesanan(self, pesanan):
        print(f"{self.nama} antar {pesanan} kepelanggan")
        self.cek_status()

    def cek_status(self):
        if len(self.pesanan_diantar) >= 5:
            self.status = "capek"
        else:
            self.status = "gasss"
        
        print(f"status pelayan {self.nama} adalah {self.status}")

if __name__ == "__main__":
    barista_1 = Barista("baon", 20, 500000)
    barista_2 = Barista("khull", 21, 500000)

    barista_1.ambil_pesanan("kopi tubruk")
    barista_1.ambil_pesanan("es kopi original")
    barista_2.ambil_pesanan("es kopi matcha")

    barista_1.antar_pesanan("kopi tubruk")
    barista_1.antar_pesanan("es kopi original")
    barista_2.antar_pesanan("es kopi matcha")