def validate(card_number: str) -> bool:
    if len(card_number) % 2 == 1:
        card_number = card_number[1:]
    card_number = [int(x) for x in card_number]
    sum_of_digits = 0
    for i in range(len(card_number)):
        if i % 2 == 0:
            card_number[i] = card_number[i] * 2
            if card_number[i] > 9:
                card_number[i] -= 9
        sum_of_digits += card_number[i]
    if sum_of_digits % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    result = validate(input("Введите номер карты: "))
    if result:
        print("Такая карта существует.")
    else:
        print("Такая карта не существует.")
