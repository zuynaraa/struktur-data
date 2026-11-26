
def insertionSort(karyawan):
    for i in range(1, len(karyawan)):
        data = karyawan[i]
        j = i - 1

        while j >= 0 and karyawan[j][1] > data[1]:
            karyawan[j + 1] = karyawan[j]
            j -= 1

        karyawan[j + 1] = data


def selectionSort(karyawan):
    for i in range(len(karyawan) - 1):
        minimum = i

        for j in range(i + 1, len(karyawan)):
            if karyawan[j][1] < karyawan[minimum][1]:
                minimum = j

        karyawan[i], karyawan[minimum] = (
            karyawan[minimum], karyawan[i]
        )


# Data karyawan: [nama, gaji]
dataKaryawan = [
    ["RARA", 3500000],
    ["KHOIR", 4500000],
    ["NISA", 3000000],
    ["ASSYAFA", 5000000],
    ["LUSI", 4000000]
]

print("=== INSERTION SORT ===")
hasilInsertion = dataKaryawan.copy()
insertionSort(hasilInsertion)

for nama, gaji in hasilInsertion:
    print(nama, "- Rp", format(gaji, ",").replace(",", "."))

print("\n=== SELECTION SORT ===")
hasilSelection = dataKaryawan.copy()
selectionSort(hasilSelection)

for nama, gaji in hasilSelection:
    print(nama, "- Rp", format(gaji, ",").replace(",", "."))
