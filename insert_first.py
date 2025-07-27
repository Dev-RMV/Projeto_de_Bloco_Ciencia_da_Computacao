from Nodes import HeadNode, Node

def insert_first(head, data):
    new_head = HeadNode(data)
    new_head.no_of_nodes = head.no_of_nodes + 1
    new_head.prev = None
    old_head = Node(head.data)
    if head.next is not None:
        head.next.prev = old_head
    old_head.next = head.next
    old_head.prev = new_head
    new_head.next = old_head
    new_head.last_node = head.last_node
    del head
    return new_head