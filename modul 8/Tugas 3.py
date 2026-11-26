# Class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Class LinkedList
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

    # Menghapus semua node
    def delete_all(self):
        temp = self.head

        while temp is not None:
            next_node = temp.next
            temp.next = None
            temp = next_node

        self.head = None


# Membuat Object LinkedList
list1 = LinkedList()

# Memasukkan data
list1.head = Node(10)
list1.head.next = Node(20)
list1.head.next.next = Node(30)
list1.head.next.next.next = Node(40)
list1.head.next.next.next.next = Node(50)

# Menampilkan data awal
print("Data sebelum dihapus:")
list1.PrintList()

# Menghapus semua node
list1.delete_all()

# Menampilkan hasil
print("\nData setelah dihapus:")
list1.PrintList()