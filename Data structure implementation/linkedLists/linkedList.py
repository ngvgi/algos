
class Node:
    def __init__(self, data: int = None) -> None:
        self.data = data
        self.next = None


class linked_list:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def length(self) -> int:
        length = 0
        curr = self.head
        while curr.next:
            length += 1
            curr = curr.next
        return length

    def print_list(self):
        if self.length() == 0:
            print('List is empty')
            return

        output = "head ->"

        curr = self.head.next
        while curr:
            output += " {} ->".format(str(curr.data))
            curr = curr.next

        output += ' null'

        return print(output)

    def get(self, index):

        if index > self.length():
            print('That index is out of range')
            return

        counter = 0
        curr = self.head
        while counter < index:
            curr = curr.next
            counter += 1

        return print('Element at index {} is {}'.format(index, curr.data))

    def delete(self, index):
        if index > self.length():
            return print('Index out of range')

        counter = 0
        curr = self.head
        while counter < index - 1:
            curr = curr.next
            counter += 1

        if curr.next.next:
            curr.next = curr.next.next
            return

        curr.next = None
    
    def insert(self, after:int, val:int) -> None:
        if self.length == 0:
            return 'List is empty, cannot insert at position'
        
        curr_val = self.head

        while curr_val.data != after:
            curr_val = curr_val.next
            if curr_val.next == None:
                print ('Cannot find element to insert after')
                return
                    
        new_node = Node(val)
        new_node.next = curr_val.next
        curr_val.next = new_node



ll = linked_list()
ll.append(4)
ll.append(23)
ll.append(3)
ll.append(54)
ll.print_list()

ll.insert(2, 6)
ll.print_list()

ll.delete(2)
ll.print_list()

ll.delete(2)
ll.print_list()

ll.delete(2)
ll.print_list()

ll.delete(1)
ll.print_list()
