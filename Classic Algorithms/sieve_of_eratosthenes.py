from typing import List


def eratosthenes(n: int) -> List[int]:
    """Generates all prime numbers to n given.

    Args:
        n (int): max number.

    Returns:
        List[int]: list of all primes.
    """
    sieve: List[int] = [x for x in range(n + 1)]
    sieve[1] = 0
    for i in range(2, n + 1):
        if i * i > n:
            break
        if sieve[i] != 0:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [x for x in sieve if sieve[x] != 0]


if __name__ == "__main__":
    eratosthenes(10_000_000)
    print("1")
