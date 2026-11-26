class Hewan:
    def __init__(self, nama, jenis, suara, makanan):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
        self.makanan = makanan

    def tampilkan_info(self):
        print("Nama    :", self.nama)
        print("Jenis   :", self.jenis)
        print("Suara   :", self.suara)
        print("Makanan :", self.makanan)
        print()


# Membuat object
hewan1 = Hewan("Milo", "Kucing", "Meong", "Ikan")
hewan2 = Hewan("Ciko", "Anjing", "Guk guk", "Daging")
hewan3 = Hewan("Kiki", "Burung", "Cuit cuit", "Biji-bijian")

# Menampilkan informasi
hewan1.tampilkan_info()
hewan2.tampilkan_info()
hewan3.tampilkan_info()