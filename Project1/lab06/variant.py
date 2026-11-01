parts = input("Целые числа через пробел: ").split()
numbers = [int(p) for p in parts]
selected = []
for number in numbers:
    if number % 2 == 0:
        selected.append(number)
print(f"Выборка: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted(selected)}")
