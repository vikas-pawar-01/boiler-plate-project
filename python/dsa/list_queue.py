from typing import Optional


class Queue:
    def __init__(self) -> None:
        self.items: list[int] = []

    def enqueue(self, value: int) -> None:
        self.items.append(value)

    def dequeue(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front element:", queue.front())
    print("Removed:", queue.dequeue())
    print("Current queue:", queue.items)
