# Node Structure
class Node:
    # Constructor untuk membuat node baru
    def __init__(self, data):
        self.data = data
        self.next = None


# Class Linked List
class LinkedList:
    # Constructor untuk membuat LinkedList kosong
    def __init__(self):
        self.head = None

    # Menampilkan isi Linked List
    def PrintList(self):
        temp = self.head

        if temp is None:
            print("Empty List!!")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

            if temp:
                print("->", end=" ")

        print()


# Membuat Object LinkedList
list1 = LinkedList()

# Membuat Object Node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Menghubungkan setiap Node
list1.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Menampilkan hasil Singly Linked List
print("Hasil Singly Linked List:")
list1.PrintList()
