class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def count_node(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

list1 = LinkedList()

list1.head = Node(10)
list1.head.next = Node(20)
list1.head.next.next = Node(30)
list1.head.next.next.next = Node(40)
list1.head.next.next.next.next = Node(50)

print("Data Linked List:")
list1.PrintList()
print("Jumlah node:", list1.count_node())