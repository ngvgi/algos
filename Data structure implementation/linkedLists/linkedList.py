
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


ll = linked_list()
ll.append(4)
ll.append(23)
ll.append(3)
ll.append(54)
ll.print_list()
ll.delete(2)
ll.print_list()
ll.delete(2)
ll.print_list()
ll.delete(2)
ll.print_list()
ll.delete(1)
ll.print_list()
