class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, val):
        self.data.append(val)
        return self.data

    def pop(self):
        if len(self.data) == 0:
            return 'The stack is empty'
        print('Removed {} from stack'.format(self.data.pop()))
        return 'New stack state: {}'.format(self.data)

    def peek(self):
        if len(self.data) == 0:
            return 'The stack is empty'
        return self.data[-1]


stack = Stack()
# print(stack.push(5))
# print(stack.push(15))
# print(stack.push(25))
# print(stack.push(35))
print(stack.peek())
print(stack.pop())


class stack_Link_List:
    def __init__(self) -> None:
        self.data = None
        self.next = None

    def push(self, data):
        if self.next is None and self.data is None:
            self.data = data
            self.next = None
            return "Current top: {}".format(self.data)

        while self.next:
            self.next = self.next
        self.data = data
        self.next = None
        return "Current top: {}".format(self.data)

    def peek(self):
        if self.data is None and self.next is None:
            return 'Stack is empty'
        while self.next:
            self.next = self.next
        return 'Stack top: {}'.format(self.data)

    def pop(self):
        if self.data is None and self.next is None:
            return 'Stack is empty'

        while self.next:
            self.next = self.next


stack2 = stack_Link_List()
print(stack2.push(5))
print(stack2.push(15))
print(stack2.push(25))
print(stack2.print_stack())
print(stack2.peek())
