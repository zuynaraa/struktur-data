class orang:
#method
    def __init__(self, nama):
        self.nama = nama

#deklarasi method
    def KatakanSalam(self):
        print("Assalamualaikum, %s" % self.nama)

org = orang ("Rahma Nur Aini")
org.KatakanSalam()