class BisaBerlari:

    def bisaLari(self):
        print("bisa larii uyy")

class BisaBerenang:

    def bisaBerenang(self):
        print("bisa reang uyy")

class Atlit(BisaBerenang, BisaBerlari):

    def __init__(self, nama):
        self.nama = nama

zambrud = Atlit("zambrud")
zambrud.bisaBerenang()
zambrud.bisaLari()

