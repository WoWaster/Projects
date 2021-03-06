from typing import List


def fibonacci(n: int) -> List[int]:
    fib: List[int] = [0, 1]
    for i in range(n - 2):
        fib.append(fib[i] + fib[i + 1])
    return fib


if __name__ == "__main__":
    print(
        fibonacci(int(input("Введите необходимое число чисел в последовательности: ")))
    )
