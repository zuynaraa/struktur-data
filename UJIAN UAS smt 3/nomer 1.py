class BarangToko:
    def __init__(self, kode_barang, nama_barang, stok, harga):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.stok = stok
        self.harga = harga

    def tambah_stok(self, jml):
        if jml <= 0:
            print(f"[!] Jumlah tambah stok harus lebih dari 0 ({self.nama_barang})")
            return
        self.stok += jml
        print(f"[+] Stok {self.nama_barang} ditambah {jml}. Stok sekarang: {self.stok}")

    def kurangi_stok(self, jml):
        if jml <= 0:
            print(f"[!] Jumlah kurangi stok harus lebih dari 0 ({self.nama_barang})")
            return
        if jml > self.stok:
            print(f"[!] Stok {self.nama_barang} tidak cukup (stok: {self.stok}, diminta: {jml})")
            return
        self.stok -= jml
        print(f"[-] Stok {self.nama_barang} dikurangi {jml}. Stok sekarang: {self.stok}")

    def total_harga(self, jumlah):
        """Total harga untuk membeli sejumlah 'jumlah' barang ini."""
        return self.harga * jumlah

    def tampil_info(self):
        print(f"Kode Barang : {self.kode_barang}")
        print(f"Nama Barang : {self.nama_barang}")
        print(f"Stok        : {self.stok}")
        print(f"Harga       : Rp{self.harga:,}".replace(",", "."))
        print("-" * 35)


# ===== Studi Kasus =====
if __name__ == "__main__":
    # 1. Buat 3 objek barang
    barang1 = BarangToko("BRG001", "Beras 5 Kg", 20, 65000)
    barang2 = BarangToko("BRG002", "Minyak Goreng 2 L", 30, 38000)
    barang3 = BarangToko("BRG003", "Gula Pasir 1 Kg", 50, 17000)

    daftar_barang = [barang1, barang2, barang3]

    print("=== INFO AWAL ===")
    for b in daftar_barang:
        b.tampil_info()

    # 2. Tambah dan kurangi stok
    print("\n=== UBAH STOK ===")
    barang1.tambah_stok(10)
    barang1.kurangi_stok(5)
    barang2.kurangi_stok(12)
    barang3.tambah_stok(25)
    barang3.kurangi_stok(100)  # contoh stok tidak cukup

    print("\n=== INFO SETELAH UBAH STOK ===")
    for b in daftar_barang:
        b.tampil_info()

    # 3. Tampilkan total nilai barang di gudang
    print("=== TOTAL NILAI BARANG DI GUDANG ===")
    total_gudang = 0
    for b in daftar_barang:
        nilai = b.total_harga(b.stok)
        total_gudang += nilai
        print(f"{b.nama_barang:<20} {b.stok:>3} x Rp{b.harga:,} = Rp{nilai:,}".replace(",", "."))
    print("-" * 55)
    print(f"Total nilai gudang : Rp{total_gudang:,}".replace(",", "."))