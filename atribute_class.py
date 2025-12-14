class Kedai:

    nama_kedai = Final = "Kedai Kopi Dimensi"
    pajak = Final = 0.15
    daftar_menu = [
        "Kopi Tubruk", "Kopi Tubruk Susu", "Es Kopi", "Es Kopi Matcha", "Es Kopi Susu"
    ]

    def __init__(self, nama_cabang, alamat, jumlah_karywan):
        self.nama_cabang = nama_cabang
        self.alamat = alamat
        self.jumlah_karywan = jumlah_karywan
        self.pendapatan_bulanan = 0.0
        self.menu_cabang = Kedai.daftar_menu.copy()

    def add_pendapatan(self, jumlah):
        pajak = jumlah * Kedai.pajak
        pendapatan_setelah_pajak = jumlah - pajak
        self.pendapatan_bulanan += pendapatan_setelah_pajak
    
    def ubah_menu(self, menu_baru):
        self.menu_cabang = menu_baru
        print(f"menu di cabang {self.menu_cabang} diubah menjadi : {menu_baru}")
        
    def info_kedai(self):
        print(f"nama kedai : {Kedai.nama_kedai}")
        print(f"nama cabang : {self.nama_cabang}")
        print(f"alamat : {self.alamat}")
        print(f"pendapatan_bulanan : {self.pendapatan_bulanan}")
        print(f"pajak : {Kedai.pajak * 100} %")
        print(f"menu_cabang : {','.join(self.menu_cabang)}")

if __name__ == "__main__":
    kedai_merjo = Kedai("Kedai Dimensi Merjo", "Merjosari-Malang", 4)
    kedai_bromo = Kedai("Kedai Dimensi Bromo", "Jln.Bromo-Malang", 6)

    kedai_merjo.add_pendapatan(1000000)
    kedai_bromo.add_pendapatan(1500000)

    kedai_bromo.ubah_menu(["kopii", "teehh"])
    kedai_merjo.info_kedai()
    kedai_bromo.info_kedai()