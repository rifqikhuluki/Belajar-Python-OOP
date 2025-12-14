class Kendaraan:

    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        return f"Merek: {self.merek}, Tahun: {self.tahun}"
    
    def nyalakan(self):
        print(f"merek: {self.merek} dinyalakan ngreeeng")

class Mobil(Kendaraan):

    def __init__(self, merek, tahun, jumlah_roda):
        super().__init__(merek, tahun)
        self.jumlah_roda = jumlah_roda

    def klaksoon(self):
        print(f"mobil: {self.info()} memiliki klaksoon tiiiin")
    
    def nyalakan(self):
        print(f"{self.merek} dinyalakan otomtis ngrreng")

class Sepeda(Kendaraan):

    def __init__(self, merek, tahun, jumlah_roda):
        super().__init__(merek, tahun)
        self.jumlah_roda = jumlah_roda

    def klaksoon(self):
        print(f"Sepeda: {self.info()} tidak memiliki klaksoon")


mobilio = Mobil("Mobilio", 2016, 4)
mobilio.nyalakan()
mobilio.klaksoon()
print(mobilio.jumlah_roda)

poligon = Sepeda("Poligon", 2016, 2)
poligon.nyalakan()
poligon.klaksoon()
print(poligon.jumlah_roda)