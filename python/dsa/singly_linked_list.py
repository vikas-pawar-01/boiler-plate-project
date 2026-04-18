from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def to_list(self) -> list[int]:
        values: list[int] = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values


if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.append(5)
    linked_list.append(15)
    linked_list.append(25)

    print("Linked list values:", linked_list.to_list())
