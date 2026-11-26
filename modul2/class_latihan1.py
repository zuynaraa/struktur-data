# Modifikasi class Mobil + 3 objek baru
 
class Mobil:
    def __init__(self, warna='Hitam', tipe='Sedan'):
        self.warna = warna
        self.tipe = tipe
        print('objek mobil telah dibuat')
 
    def maju(self):
        print('maju')
 
    def mundur(self):
        print('mundur')
 
    def melaju(self, speed):
        print('mobil melaju dengan kecepatan %s km/jam' % speed)
 
    def info(self):
        print('Mobil %s berwarna %s' % (self.tipe, self.warna))
 
 
# objek pertama (pakai nilai default)
mobil1 = Mobil()
print(mobil1.warna)
mobil1.maju()
mobil1.melaju(100)
 
# 3 objek baru
mobil2 = Mobil('Merah', 'SUV')
mobil2.info()
mobil2.maju()
mobil2.melaju(80)
 
mobil3 = Mobil('Putih', 'Hatchback')
mobil3.info()
mobil3.mundur()
mobil3.melaju(60)
 
mobil4 = Mobil('Biru', 'Truk')
mobil4.info()
mobil4.maju()
mobil4.melaju(40)