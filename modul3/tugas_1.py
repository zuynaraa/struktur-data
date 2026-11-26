def l_search(a, x, l, n):
    if l < n:
        if a[l] == x:
            print("Data", x, "ditemukan pada index", l)
        else:
            l_search(a, x, l + 1, n)
    else:
        print("Data tidak ditemukan")

print("Masukkan list data:")
a = [int(b) for b in input().split()]
x = int(input("Masukkan data yang dicari: "))
n = len(a)
l_search(a, x, 0, n)