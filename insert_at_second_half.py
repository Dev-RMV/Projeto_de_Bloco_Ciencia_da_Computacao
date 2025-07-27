from Nodes import Node
def insert_at_second_half(head, data ,aux_mid):
    new_node = Node(data)
    while True:
        if aux_mid.next is None:
            new_node.prev = aux_mid
            aux_mid.next = new_node
            head.no_of_nodes = head.no_of_nodes + 1
            head.last_node = new_node
            return head
        elif aux_mid.data <= data <= aux_mid.next.data:
            new_node.prev = aux_mid
            new_node.next = aux_mid.next
            aux_mid.next.prev = new_node
            aux_mid.next = new_node
            head.no_of_nodes = head.no_of_nodes + 1
            return head
        elif aux_mid.data < data and aux_mid.next.data < data:
            aux_mid = aux_mid.next