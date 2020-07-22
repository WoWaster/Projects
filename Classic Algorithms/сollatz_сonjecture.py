def collatz(num: int) -> int:
    """Perform collatz algorithm and count number of step it took to came to 1.

    Args:
        num (int): number to process.

    Returns:
        int: number of steps to come to one.
    """
    counter: int = 0
    while num != 1:
        if num % 2 == 0:
            counter = counter + 1
            num = num // 2
        elif num % 2 == 1:
            counter = counter + 1
            num = num * 3 + 1
    return counter


if __name__ == "__main__":
    n = collatz(int(input("Введите число: ")))
    print("Число пришло к единице за", n, "шагов.")
