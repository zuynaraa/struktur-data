
def bubbleSort(data):
    n = len(data)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


panjang = int(input("Masukkan jumlah data = "))
data = []

for i in range(panjang):
    angka = int(input(f"Masukkan data ke-{i + 1} = "))
    data.append(angka)

print("Sebelum Bubble Sort =", data)

bubbleSort(data)

print("Setelah Bubble Sort =", data)
