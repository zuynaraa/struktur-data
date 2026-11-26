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

    # Insert data sebelum data tertentu
    def insert_before_data(self, x, data):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.data:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return

        n = self.head

        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next

        if n.next is None:
            print("item not in the list")
        else:
            temp = Node(data)
            temp.next = n.next
            n.next = temp


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

# 6. Insert data sebelum 20
list1.insert_before_data(20, 15)

print("Setelah insert sebelum 20:")
list1.PrintList()

# 7. Insert data sebelum 40
list1.insert_before_data(40, 35)

print("Setelah insert sebelum 40:")
list1.PrintList()
