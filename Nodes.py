class HeadNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.no_of_nodes = 1
        self.last_node = self

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None