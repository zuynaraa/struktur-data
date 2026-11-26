data_awal = [
    ("B001", "Komputer", "Elektronik", 15),
    ("B002", "Monitor", "Elektronik", 10),
    ("B003", "Keyboard", "Aksesori", 20),
    ("B004", "Mouse", "Aksesori", 25),
    ("B005", "Proyektor", "Elektronik", 3),
]

inventaris = {}
for kode, nama, kategori, jumlah in data_awal:
    inventaris[kode] = (nama, kategori, jumlah)


def tampilkan_semua():
    print("\n" + "=" * 62)
    print(f"{'Kode':<8}{'Nama Barang':<18}{'Kategori':<14}{'Jumlah':>8}")
    print("=" * 62)
    for kode, (nama, kategori, jumlah) in inventaris.items():
        print(f"{kode:<8}{nama:<18}{kategori:<14}{jumlah:>8}")
    print("=" * 62)


def tambah_barang():
    kode = input("Kode barang  : ").strip().upper()
    if kode == "":
        print("[!] Kode barang tidak boleh kosong")
        return
    if kode in inventaris:  
        print(f"[!] Gagal: kode barang {kode} sudah digunakan ({inventaris[kode][0]})")
        return
    nama = input("Nama barang  : ").strip()
    kategori = input("Kategori     : ").strip().title()
    if nama == "" or kategori == "":
        print("[!] Nama dan kategori tidak boleh kosong")
        return
    try:
        jumlah = int(input("Jumlah       : "))
        if jumlah < 0:
            raise ValueError
    except ValueError:
        print("[!] Jumlah harus berupa angka bulat >= 0")
        return
    inventaris[kode] = (nama, kategori, jumlah)
    print(f"[+] Barang {kode} - {nama} berhasil ditambahkan")


def cari_barang():
    kode = input("Kode barang yang dicari: ").strip().upper()
    if kode in inventaris:
        nama, kategori, jumlah = inventaris[kode]
        print("\nBarang ditemukan:")
        print(f"Kode     : {kode}")
        print(f"Nama     : {nama}")
        print(f"Kategori : {kategori}")
        print(f"Jumlah   : {jumlah}")
    else:
        print(f"[!] Barang dengan kode {kode} tidak ditemukan")


def total_unit():
    total = 0
    for nama, kategori, jumlah in inventaris.values():
        total += jumlah
    print(f"\nTotal seluruh unit barang: {total} unit")


def tampilkan_kategori():
    kategori_unik = set()
    for nama, kategori, jumlah in inventaris.values():
        kategori_unik.add(kategori)
    print(f"\nKategori barang ({len(kategori_unik)} kategori):")
    for k in sorted(kategori_unik):
        print(f"- {k}")


def menu():
    print("\n===== INVENTARIS LABORATORIUM KOMPUTER =====")
    print("1. Tampilkan seluruh barang")
    print("2. Tambah barang baru")
    print("3. Cari barang berdasarkan kode")
    print("4. Hitung total seluruh unit barang")
    print("5. Tampilkan kategori barang (tanpa duplikasi)")
    print("0. Keluar")


def main():
    while True:
        menu()
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            tampilkan_semua()
        elif pilih == "2":
            tambah_barang()
        elif pilih == "3":
            cari_barang()
        elif pilih == "4":
            total_unit()
        elif pilih == "5":
            tampilkan_kategori()
        elif pilih == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("[!] Menu tidak valid")


if __name__ == "__main__":
    main()