class Node:
    """
    Node class for creating a node for a linked list
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    """
    Simple class to create linked list objects that links together Node objects
    """
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if not current:
            raise ValueError(f'{data} not in list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError(f"{data} not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


llist = LinkedList()

llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)

llist.head.get_next()

def reverseLList(head):
    if head == None:
        return
    reverseLList(head.get_next())
    print(head.get_data())

reverseLList(llist.head)

