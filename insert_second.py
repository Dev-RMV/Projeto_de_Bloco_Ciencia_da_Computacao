from Nodes import Node

def insert_second(head, data):
    head.next = new_node = Node(data)
    head.no_of_nodes = head.no_of_nodes + 1
    new_node.prev = head
    head.last_node = new_node
    return head