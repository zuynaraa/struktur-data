
def bubbleSort(data):
    n = len(data)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j][1] < data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]


mahasiswa = []

# Input data 20 mahasiswa
for i in range(5):
    print(f"\nMahasiswa ke-{i + 1}")
    nama = input("Nama mahasiswa = ")

    basisData = float(input("Nilai Basis Data = "))
    sistemOperasi = float(input("Nilai Sistem Operasi = "))
    strukturData = float(input("Nilai Struktur Data = "))

    mahasiswa.append([
        nama, basisData, sistemOperasi, strukturData
    ])


mataKuliah = [
    ("Basis Data", 1),
    ("Sistem Operasi", 2),
    ("Struktur Data", 3)
]

# Mengurutkan dan menampilkan 5 mahasiswa terbaik
for namaMK, indeksNilai in mataKuliah:
    ranking = []

    for mhs in mahasiswa:
        ranking.append([mhs[0], mhs[indeksNilai]])

    bubbleSort(ranking)

    print(f"\n=== 5 MAHASISWA TERBAIK: {namaMK} ===")
    print("Peringkat | Nama | Nilai")

    for i in range(5):
        print(
            f"{i + 1} | {ranking[i][0]} | {ranking[i][1]}"
        )
