# 1. Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 2. Class LinkedList
class LinkedList:
    def __init__(self):
        self.head = None

    # Menampilkan isi Linked List
    def PrintList(self):
        temp = self.head

        if temp is None:
            print("Empty List!!")
            return

        while temp:
            print(temp.data, end="")
            temp = temp.next

            if temp:
                print(" -> ", end="")

        print()

    # Delete data di awal
    def del_front(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None


# 3. Membuat Object LinkedList
list1 = LinkedList()

# 4. Memasukkan data awal
list1.head = Node(10)
list1.head.next = Node(20)
list1.head.next.next = Node(30)
list1.head.next.next.next = Node(40)
list1.head.next.next.next.next = Node(50)

# 5. Menampilkan data awal
print("Data awal:")
list1.PrintList()

# 6. Menghapus data di awal
list1.del_front()

# 7. Menampilkan hasil
print("Setelah delete data di awal:")
list1.PrintList()
