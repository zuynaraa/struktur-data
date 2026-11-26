class persegi_panjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)


# membuat objek
pp1 = persegi_panjang(10, 5)
print("Panjang persegi panjang:", pp1.panjang)
print("Lebar persegi panjang:", pp1.lebar)
print("Luas persegi panjang:", pp1.luas())
print("Keliling persegi panjang:", pp1.keliling())

pp2 = persegi_panjang(7, 3)
print("Luas persegi panjang:", pp2.luas())
print("Keliling persegi panjang:", pp2.keliling())