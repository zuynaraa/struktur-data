# Class Kucing
 
class Kucing:
    def __init__(self, umur, warna_bulu):
        self._umur = umur
        self.warna_bulu = warna_bulu
 
    def meong(self):
        print('Meong... meong...')
 
    def umur(self):
        print('Umur kucing ini %s tahun' % self._umur)
 
 
print()
print('--- Objek Kucing ---')
 
kucing1 = Kucing(2, 'Oranye')
print('Warna bulu:', kucing1.warna_bulu)
kucing1.meong()
kucing1.umur()
 
kucing2 = Kucing(5, 'Hitam')
print('Warna bulu:', kucing2.warna_bulu)
kucing2.meong()
kucing2.umur()