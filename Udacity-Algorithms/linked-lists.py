class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def printList(self):
        current = self.head
        if self.head:
            while current.next:
                print(current.value)
                current = current.next
            print(current.value)
        else:
            print('No list elements')

ll = LinkedList()
for i in range(0,10):
    elm = Element(i)
    ll.append(elm)


ll.printList()
