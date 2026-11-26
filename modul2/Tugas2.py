class Mahasiswa:

    def __init__(self, nama, nim, alamat, semester):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.semester = semester

    def tampilkanNama(self):
        print("Nama     :", self.nama)

    def tampilkanNim(self):
        print("NIM      :", self.nim)

    def tampilkanAlamat(self):
        print("Alamat   :", self.alamat)

    def tampilkanSemester(self):
        print("Semester :", self.semester)


# Membuat object mahasiswa
mhs1 = Mahasiswa(
    "Rahma Nur Aini",
    "1202507008",
    "Singapura",
    3
)

# Menampilkan data
mhs1.tampilkanNama()
mhs1.tampilkanNim()
mhs1.tampilkanAlamat()
mhs1.tampilkanSemester()