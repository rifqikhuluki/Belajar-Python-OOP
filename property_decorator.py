class Kategori:
    __name = ""

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Ojo Kosong Nyook")
        else:
            self.__name = name

kategori1 = Kategori()
kategori1.name = "Kopii"
print(kategori1.name)