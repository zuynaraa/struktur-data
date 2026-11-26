class Orang:

    total = 0

    def __init__(self, nama):
        self.nama = nama
        Orang.total += 1

    def __del__(self):
        Orang.total -= 1

    def katakan_hallo(self):
        print("Hallo, nama saya", self.nama, ", apa kabar?")

    def total_populasi(cls):
        print("Total Orang adalah", cls.total)

    total_populasi = classmethod(total_populasi)


org1 = Orang("Rahma Nur Aini")
org1.katakan_hallo()
Orang.total_populasi()

org2 = Orang("Aulia")
org2.katakan_hallo()
Orang.total_populasi()

print("Objek org1 dihapus")
del org1
del org2

Orang.total_populasi()