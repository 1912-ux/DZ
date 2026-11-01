from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input("Целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    numbers = [int(p) for p in input("Целые числа через пробел: ").split()]
    avg = average(numbers)
    if avg is None:
        print("Нет данных")
    else:
        print(f"Среднее: {avg:.2f}")

    text = input("Произвольный текст: ")
    print(f"Нормализованный текст: {normalize_text(text)}")

    threshold = int(input("Порог (неотрицательное целое): "))
    print(f"Выборка: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()