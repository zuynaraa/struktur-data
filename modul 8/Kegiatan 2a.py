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

    # A. Insert data di awal
    def insert_at_start(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    # Insert data di akhir
    def insert_at_end(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        n = self.head

        while n.next is not None:
            n = n.next

        n.next = temp

    # Insert data setelah data tertentu
    def insert_after_data(self, x, data):
        n = self.head

        while n is not None:
            if n.data == x:
                break
            n = n.next

        if n is None:
            print("item not in the list")
        else:
            temp = Node(data)
            temp.next = n.next
            n.next = temp

    # B. Insert data sebelum data tertentu
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
list1.insert_at_end(10)
list1.insert_at_end(20)
list1.insert_at_end(30)
list1.insert_at_end(40)

# 5. Menampilkan data awal
print("Data awal:")
list1.PrintList()

# 6. Insert data di awal
list1.insert_at_start(5)
print("Setelah insert di awal:")
list1.PrintList()

# 7. Insert data di akhir
list1.insert_at_end(50)
print("Setelah insert di akhir:")
list1.PrintList()

# 8. Insert setelah data tertentu
list1.insert_after_data(20, 25)
print("Setelah insert setelah 20:")
list1.PrintList()

# 9. Insert sebelum data tertentu
list1.insert_before_data(30, 27)
print("Setelah insert sebelum 30:")
list1.PrintList()
