from typing import Optional


class Stack:
    def __init__(self) -> None:
        self.items: list[int] = []

    def push(self, value: int) -> None:
        self.items.append(value)

    def pop(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self) -> Optional[int]:
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())
    print("Removed:", stack.pop())
    print("Current stack:", stack.items)
