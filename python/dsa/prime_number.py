def is_prime(number: int) -> bool:
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def primes_up_to(limit: int) -> list[int]:
    return [number for number in range(2, limit + 1) if is_prime(number)]


if __name__ == "__main__":
    number = 29
    limit = 50

    print(f"Is {number} prime? {is_prime(number)}")
    print(f"Primes up to {limit}: {primes_up_to(limit)}")
