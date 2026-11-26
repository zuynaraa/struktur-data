class Pasien:
    def __init__(self, id_pasien, nama, keluhan):
        self.id_pasien = id_pasien
        self.nama = nama
        self.keluhan = keluhan

    def __str__(self):
        return f"ID: {self.id_pasien} | Nama: {self.nama} | Keluhan: {self.keluhan}"


class AntreanPasien:
    """Queue (FIFO): masuk di belakang (enqueue), dilayani dari depan (dequeue)."""

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, pasien):
        self.data.append(pasien)
        print(f"[+] {pasien.nama} masuk antrean nomor {len(self.data)}")

    def dequeue(self):
        if self.is_empty():
            print("[!] Antrean kosong, tidak ada pasien yang dilayani")
            return None
        pasien = self.data.pop(0)
        print(f"[>] Melayani pasien: {pasien}")
        return pasien

    def linear_search(self, nama_dicari):
        """Cari pasien berdasarkan nama (tidak peka huruf besar/kecil).
        Mengembalikan list (posisi antrean, pasien)."""
        hasil = []
        for i in range(len(self.data)):
            if nama_dicari.lower() in self.data[i].nama.lower():
                hasil.append((i + 1, self.data[i]))
        return hasil

    def tampilkan(self):
        if self.is_empty():
            print("Antrean kosong")
            return
        print(f"\n=== DAFTAR ANTREAN ({len(self.data)} pasien) ===")
        for i, p in enumerate(self.data, start=1):
            print(f"{i}. {p}")
        print()


def menu():
    print("\n===== ANTREAN PENDAFTARAN PASIEN KLINIK =====")
    print("1. Tambah pasien ke antrean")
    print("2. Layani pasien (dequeue)")
    print("3. Cari pasien berdasarkan nama")
    print("4. Tampilkan antrean")
    print("0. Keluar")


def main():
    antrean = AntreanPasien()
    nomor = 1  # id_pasien otomatis

    # Data awal agar mudah disimulasikan
    for nama, keluhan in [("Budi Santoso", "Demam"),
                          ("Siti Aminah", "Batuk dan pilek"),
                          ("Andi Wijaya", "Sakit kepala")]:
        antrean.enqueue(Pasien(f"P{nomor:03d}", nama, keluhan))
        nomor += 1

    while True:
        menu()
        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            nama = input("Nama pasien    : ").strip()
            keluhan = input("Keluhan        : ").strip()
            if not nama:
                print("[!] Nama tidak boleh kosong")
                continue
            antrean.enqueue(Pasien(f"P{nomor:03d}", nama, keluhan))
            nomor += 1

        elif pilih == "2":
            antrean.dequeue()

        elif pilih == "3":
            cari = input("Nama yang dicari: ").strip()
            hasil = antrean.linear_search(cari)
            if hasil:
                print(f"\nDitemukan {len(hasil)} pasien:")
                for posisi, p in hasil:
                    print(f"- Antrean ke-{posisi}: {p}")
            else:
                print(f"[!] Pasien dengan nama '{cari}' tidak ditemukan di antrean")

        elif pilih == "4":
            antrean.tampilkan()

        elif pilih == "0":
            print("Terima kasih, program selesai.")
            break

        else:
            print("[!] Menu tidak valid")


if __name__ == "__main__":
    main()