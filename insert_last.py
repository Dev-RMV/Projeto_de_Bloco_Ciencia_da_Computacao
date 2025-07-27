from Nodes import Node

def insert_last(head, data):
    new_node = Node(data)
    new_node.prev = head.last_node
    head.last_node.next = new_node
    head.last_node = new_node
    head.no_of_nodes = head.no_of_nodes + 1
    return head