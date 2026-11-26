class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def PrintList(self):
        temp = self.head
        if temp is None:
            print("List Kosong!!")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp:
                print("<->", end=" ")
        print()


# Membuat objek LinkedList
list1 = LinkedList()

# Membuat node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Menghubungkan node
list1.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

# Menampilkan linked list
list1.PrintList()