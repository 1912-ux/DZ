parts = input("Целые числа через пробел: ").split()
if not parts:
    print("Нет данных")
else:
    numbers = [int(p) for p in parts]
    maximum = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)
    print(positions)