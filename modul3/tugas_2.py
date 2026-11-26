def b_search(a, x, low, high):
    if low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            print("Data", x, "ditemukan pada index", mid)
        elif x > a[mid]:
            b_search(a, x, low, mid - 1)    
        else:
            b_search(a, x, mid + 1, high)   
    else:
        print("Data tidak ditemukan")

print("Masukkan list data:")
a = [int(b) for b in input().split()]
a.sort(reverse=True)                        
print("List setelah diurutkan:", a)
x = int(input("Masukkan data yang dicari: "))
b_search(a, x, 0, len(a) - 1)