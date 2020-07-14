def power(n: float, k: int) -> float:
    if k == 0:
        return 1
    if k < 0:
        n = 1 / n
        k = -k
    result = 1
    while k != 1:
        if k % 2 == 0:
            n = n * n
            k = k // 2
        else:
            result = result * n
            n = n * n
            k = (k - 1) // 2
    return result * n


if __name__ == "__main__":
    print(f"78 to the power of 25 is {power(78, 25)}.")
    print(power(2, 10))
    print(power(5, -2))
    print(power(0.5, 2))
