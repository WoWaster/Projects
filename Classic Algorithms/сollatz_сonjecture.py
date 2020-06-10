def count_steps(num: int) -> int:
    counter = 0
    while num != 1:
        if num % 2 == 0:
            counter = counter + 1
            num = num / 2
        elif num % 2 == 1:
            counter = counter + 1
            num = num * 3 + 1
    return counter


if __name__ == "__main__":
    n = count_steps(int(input("Введите число: ")))
    print("Число пришло к единице за", n, "шагов.")
