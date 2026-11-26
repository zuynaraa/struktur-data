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

    # Mencari data tertentu
    def search_data(self, data):
        temp = self.head
        index = 0

        while temp is not None:
            if temp.data == data:
                print("Data ditemukan pada index ke", index)
                return index

            temp = temp.next
            index += 1

        print("Data tidak ditemukan")
        return -1


# Membuat Object LinkedList
list1 = LinkedList()

# Memasukkan data
list1.head = Node(10)
list1.head.next = Node(20)
list1.head.next.next = Node(30)
list1.head.next.next.next = Node(40)
list1.head.next.next.next.next = Node(50)

# Menampilkan data
print("Data Linked List:")
list1.PrintList()

# Mencari data
print("\nMencari data 20:")
list1.search_data(20)
