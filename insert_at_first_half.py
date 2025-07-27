from Nodes import Node
def insert_at_first_half(head, data ,aux_mid):
    new_node = Node(data)
    while True:
        if aux_mid.prev.data <= data <= aux_mid.data:
            new_node.next = aux_mid
            new_node.prev = aux_mid.prev
            aux_mid.prev.next = new_node
            aux_mid.prev = new_node
            head.no_of_nodes = head.no_of_nodes + 1
            return head
        elif aux_mid.data > data and aux_mid.prev.data > data:
            aux_mid = aux_mid.prev