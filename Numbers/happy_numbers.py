from typing import List, Set


def happy_number(n: int) -> int:
    steps: Set[int] = set()
    n_initial: int = n
    while n not in steps:
        n_sum: int = 0
        steps.add(n)
        while n > 0:
            n_sum += (n % 10) ** 2
            n //= 10
        if n_sum == 1:
            return n_initial
        n = n_sum
    return 0


if __name__ == "__main__":
    nums: List[int] = []
    for i in range(1000):
        num = happy_number(i)
        if num != 0:
            nums.append(num)
    print(nums)
    print(len(nums))
