class Karyawan:

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class KaryawanTetap(Karyawan):
    pass

class Kitchen(KaryawanTetap):
    pass

class Barista(Kitchen):
    pass