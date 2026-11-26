import os
from openpyxl import load_workbook

# Baca data dari Excel di folder yang sama dengan file .py ini
lokasi = os.path.join(os.path.dirname(__file__), "data_mahasiswa.xlsx")
ws = load_workbook(lokasi).active
mahasiswa = [list(baris) for baris in ws.iter_rows(min_row=2, values_only=True)]
mahasiswa = [list(baris) for baris in ws.iter_rows(min_row=2, values_only=True)]

def m_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        l_half = a[:mid]
        r_half = a[mid:]
        m_sort(l_half)
        m_sort(r_half)
        i = j = k = 0
        while i < len(l_half) and j < len(r_half):
            if l_half[i][2].lower() <= r_half[j][2].lower():
                a[k] = l_half[i]
                i += 1
            else:
                a[k] = r_half[j]
                j += 1
            k += 1
        while i < len(l_half):
            a[k] = l_half[i]
            i += 1
            k += 1
        while j < len(r_half):
            a[k] = r_half[j]
            j += 1
            k += 1

print("Data sebelum diurutkan:")
for m in mahasiswa:
    print(m)

m_sort(mahasiswa)

print("\nData setelah diurutkan berdasarkan Asal (Merge Sort):")
for m in mahasiswa:
    print(m)