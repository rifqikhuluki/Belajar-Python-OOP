class Product :

    def __init__(self, id_product, name, base_price):
        self.__id_product = id_product
        self.name = name
        self.__base_price = base_price

    def getterId(self) :
        return self.__id_product
    
    def getterPrice(self) :
        return self.__base_price
    
    def displayDetail(self) :
        print(f"Product Detail :")
        print(f"ID : {self.getterId()}")
        print(f"Name : {self.name}")
        print(f"Price : Rp.{self.getterPrice()}")

class Smartphone(Product) :
    
    def __init__(self, id_product, name, base_price, screen_size, batery_capacity):
        super().__init__(id_product, name, base_price)
        self.screen_size = screen_size
        self.batery_capacity = batery_capacity

    def displayDetail(self):
        super().displayDetail()
        print(f"Type : Smartphone")
        print(f"Screen Size : {self.screen_size} inches")
        print(f"Batery Capacity : {self.batery_capacity} mAh")
        print("------------------------------")

class Laptop(Product) :

    def __init__(self, id_product, name, base_price, ram_size, processor):
        super().__init__(id_product, name, base_price)
        self.ram_size = ram_size
        self.processor = processor
    
    def displayDetail(self):
        super().displayDetail()
        print(f"Type : Laptop")
        print(f"Ram Size : {self.ram_size} GB")
        print(f"Processor : {self.processor}")
        print("------------------------------")

# class InvetoryApp :
#     def __init__(self):
#         self.products = []
    
#     def addProduct(self, product) :
#         self.products.append(product)
    
#     def displayInventory(self) :
#         print("----- Product  Invebtory -----")

#         for product in self.products :
#             product.displayDetail()

if __name__ == "__main__":
# class InventoryApp :

    smartphone1 = Smartphone("S001", "Samsung asekk", "10000000", "6.5", "45000")
    laptop1 = Laptop("HP", "Victus", "14000000", "16", "Intel i7")

    products = [smartphone1, laptop1]
    
    print("----- Product  Invebtory -----")
    for product in products :
        product.displayDetail()

    smartphone1.getterId()
    print(smartphone1)





