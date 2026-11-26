def bubble_sort(data):
    """Mengurutkan list dari terkecil ke terbesar (ascending) tanpa sort()/sorted()."""
    hasil = data[:]  # salinan, agar list asli tidak berubah
    n = len(hasil)
    for i in range(n - 1):
        ada_tukar = False
        for j in range(n - 1 - i):
            if hasil[j] > hasil[j + 1]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
                ada_tukar = True
        if not ada_tukar:  # sudah terurut, berhenti lebih awal
            break
    return hasil


def nilai_tertinggi(data):
    tertinggi = data[0]
    for x in data:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


def nilai_terendah(data):
    terendah = data[0]
    for x in data:
        if x < terendah:
            terendah = x
    return terendah


def rata_rata(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)


def tampilkan_statistik(data):
    print(f"Hasil pengurutan : {data}")
    print(f"Nilai tertinggi  : {nilai_tertinggi(data)}")
    print(f"Nilai terendah   : {nilai_terendah(data)}")
    print(f"Rata-rata        : {rata_rata(data):.2f}")


if __name__ == "__main__":
    nilai = [75, 90, 65, 85, 70, 95, 80]

    # 1. Tampilkan nilai sebelum diurutkan
    print("=== 1. SEBELUM DIURUTKAN ===")
    print(f"Data awal        : {nilai}")

    # 2 & 3. Bubble Sort + tampilkan hasil, tertinggi, terendah, rata-rata
    print("\n=== 2 & 3. SETELAH BUBBLE SORT ===")
    terurut = bubble_sort(nilai)
    tampilkan_statistik(terurut)

    # 4. Tambahkan nilai 88, urutkan kembali, tampilkan hasil akhir
    print("\n=== 4. TAMBAH NILAI 88 ===")
    terurut.append(88)
    print(f"Setelah ditambah 88 (belum diurutkan ulang): {terurut}")
    terurut = bubble_sort(terurut)
    print()
    tampilkan_statistik(terurut)