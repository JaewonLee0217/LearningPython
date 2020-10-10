class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return not bool(self.items)

    def push(self,value):
        self.items.append(value)

    def size(self):
        return len(self.items)

    def __repr__(self):
        return '{}'.format(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]

        else:
            print('Stack is empty')
            return None

    def pop(self):
        value = self.items.pop()
        if value is not None:
            return value
        else:
            return 'Stack is empty'

if __name__ == '__main__':
    stack = Stack()
    print(stack.isEmpty())
    stack.push(5)
    stack.push(6)
    stack.push(7)
    print(stack)
