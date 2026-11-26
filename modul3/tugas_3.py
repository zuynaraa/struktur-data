# Data ID pemilih yang sudah terdaftar
data_id = [1045, 1012, 1088, 1003, 1067, 1021, 1099]

# ---------- Linear Search ----------
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# ---------- Binary Search (data harus terurut menaik) ----------
def binary_search(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# ---------- Program utama ----------
id_pemilih = int(input("Masukkan nomor ID pemilih: "))

print("\n=== Linear Search ===")
hasil = linear_search(data_id, id_pemilih)
if hasil != -1:
    print("ID", id_pemilih, "TERDAFTAR (index", hasil, ")")
else:
    print("ID", id_pemilih, "TIDAK TERDAFTAR")

print("\n=== Binary Search ===")
data_urut = sorted(data_id)          
print("Data setelah diurutkan:", data_urut)
hasil = binary_search(data_urut, id_pemilih)
if hasil != -1:
    print("ID", id_pemilih, "TERDAFTAR (index", hasil, ")")
else:
    print("ID", id_pemilih, "TIDAK TERDAFTAR")