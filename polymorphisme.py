class Hewan:

    def __init__(self, nama):
        self.nama = nama
    
    def bersuara(self):
        print(f"{self.nama} bersuara")

class Sapi(Hewan):

    def bersuara(self):
        print(f"{self.nama} moooooo")

class Kucing(Hewan):

    def bersuara(self):
        print(f"{self.nama} meoouung")

class Anjing(Hewan):

    def bersuara(self):
        print(f"{self.nama} pinjam seratus dong cuy")

hewan_list = [
    Sapi("dancow"),
    Kucing("Oreeen"),
    Anjing("Yang merasa")
]

for hewan in hewan_list:
    hewan.bersuara()