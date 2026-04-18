EXAMPLES: dict[str, str] = {
    "prime": "dsa/prime_number.py",
    "stack": "dsa/list_stack.py",
    "queue": "dsa/list_queue.py",
    "linked_list": "dsa/singly_linked_list.py",
}


def print_examples() -> None:
    print("Available DSA examples:")
    for name, path in EXAMPLES.items():
        print(f"- {name}: python {path}")


if __name__ == "__main__":
    print_examples()
