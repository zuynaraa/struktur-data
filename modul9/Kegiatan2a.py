def insert_first(self, data):
    new = Node(data)
    if(self.head == None):
        self.head = new
        return
    else:
        self.head.prev = new
        new.next = self.head
        self.head = new