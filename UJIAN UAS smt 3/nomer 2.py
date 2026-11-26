class Node:
    def __init__(self, judul, penyanyi, durasi):
        self.judul = judul
        self.penyanyi = penyanyi
        self.durasi = durasi  # dalam menit
        self.prev = None
        self.next = None


class Playlist:
    """Double Linked List untuk simulasi playlist musik."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None  # lagu yang sedang diputar
        self.size = 0

    # 1. Tambah lagu di akhir
    def tambah_di_akhir(self, judul, penyanyi, durasi):
        baru = Node(judul, penyanyi, durasi)
        if self.head is None:
            self.head = self.tail = self.current = baru
        else:
            baru.prev = self.tail
            self.tail.next = baru
            self.tail = baru
        self.size += 1
        print(f"[+] Ditambahkan: {judul} - {penyanyi}")

    # 2. Hapus lagu di awal
    def hapus_di_awal(self):
        if self.head is None:
            print("[!] Playlist kosong")
            return
        dihapus = self.head
        if self.head == self.tail:  # hanya 1 lagu
            self.head = self.tail = self.current = None
        else:
            self.head = self.head.next
            self.head.prev = None
            if self.current == dihapus:
                self.current = self.head
        self.size -= 1
        print(f"[-] Dihapus: {dihapus.judul} - {dihapus.penyanyi}")

    # 3. Navigasi maju dan mundur
    def next(self):
        if self.current is None:
            print("[!] Playlist kosong")
        elif self.current.next is None:
            print("[!] Sudah di lagu terakhir")
        else:
            self.current = self.current.next
            print(f">> NEXT     : {self.current.judul} - {self.current.penyanyi}")

    def previous(self):
        if self.current is None:
            print("[!] Playlist kosong")
        elif self.current.prev is None:
            print("[!] Sudah di lagu pertama")
        else:
            self.current = self.current.prev
            print(f"<< PREVIOUS : {self.current.judul} - {self.current.penyanyi}")

    # 4. Tampilkan seluruh daftar lagu
    def tampilkan(self):
        if self.head is None:
            print("Playlist kosong")
            return
        print(f"\n=== DAFTAR PLAYLIST ({self.size} lagu) ===")
        temp = self.head
        no = 1
        while temp:
            tanda = "  <- sedang diputar" if temp == self.current else ""
            print(f"{no}. {temp.judul} - {temp.penyanyi} ({temp.durasi} menit){tanda}")
            temp = temp.next
            no += 1
        print()


# ===== Simulasi =====
if __name__ == "__main__":
    pl = Playlist()

    # Minimal 5 lagu
    pl.tambah_di_akhir("Impossible", "James Arthur", 3.4)
    pl.tambah_di_akhir("Jakarta Hari Ini", "For Revenge & Stereo Wall", 4.0)
    pl.tambah_di_akhir("Shape of My Heart", "Sting", 4.6)
    pl.tambah_di_akhir("1000x", "Ghea Indrawari", 3.9)
    pl.tambah_di_akhir("Treat You Better", "Shawn Mendes", 3.2)
    pl.tampilkan()

    print("--- Simulasi Next ---")
    pl.next()
    pl.next()
    pl.next()
    pl.tampilkan()

    print("--- Simulasi Previous ---")
    pl.previous()
    pl.previous()
    pl.tampilkan()

    print("--- Hapus lagu di awal ---")
    pl.hapus_di_awal()
    pl.tampilkan()

    print("--- Next lagi sampai ujung, lalu Previous ---")
    pl.next()
    pl.next()
    pl.next()
    pl.next()
    pl.next()  # sudah di lagu terakhir
    pl.previous()
    pl.tampilkan()