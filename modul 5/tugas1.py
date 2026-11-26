import os
from openpyxl import load_workbook

# Baca data dari Excel di folder yang sama dengan file .py ini
lokasi = os.path.join(os.path.dirname(__file__), "data_mahasiswa.xlsx")
ws = load_workbook(lokasi).active
mahasiswa = [list(baris) for baris in ws.iter_rows(min_row=2, values_only=True)]

def q_sort(a, low, high):
    if low < high:
        pivotpos = partition(a, low, high)
        q_sort(a, low, pivotpos - 1)
        q_sort(a, pivotpos + 1, high)

def partition(a, low, high):
    pivotvalue = a[low][1]
    up = low + 1
    down = high
    done = False
    while not done:
        while up <= down and a[up][1] <= pivotvalue:
            up += 1
        while down >= up and a[down][1] >= pivotvalue:
            down -= 1
        if down < up:
            done = True
        else:
            temp = a[up]
            a[up] = a[down]
            a[down] = temp
    temp = a[low]
    a[low] = a[down]
    a[down] = temp
    return down

print("Data sebelum diurutkan:")
for m in mahasiswa:
    print(m)

q_sort(mahasiswa, 0, len(mahasiswa) - 1)

print("\nData setelah diurutkan berdasarkan NIM (Quick Sort):")
for m in mahasiswa:
    print(m)