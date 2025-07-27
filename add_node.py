from create_head import create_head
from insert_first import insert_first
from insert_second import insert_second
from insert_last import insert_last
from insert_at_second_half import insert_at_second_half
from insert_at_first_half import insert_at_first_half


def add_node(head, data):
    if head is None:
        return create_head(data)
    if data <= head.data:
        return insert_first(head, data)
    if head.next is None:
        return insert_second(head, data)
    if head.last_node.data <= data:
        return insert_last(head, data)
    else:
        aux_mid = head
        for i in range(round(head.no_of_nodes / 2)):
            aux_mid = aux_mid.next if aux_mid.next is not None else aux_mid

        if aux_mid.data <= data:
            return insert_at_second_half(head, data, aux_mid)
        if aux_mid.data > data:
            return insert_at_first_half(head, data, aux_mid)
    return None
