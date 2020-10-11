class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = None
class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return not bool(self.head)
