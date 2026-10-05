n = int(input("Сколько чисел: "))

total = 0
positive_count = 0
maximum = None #Пометка для себя: None - ещё не задан.

for i in range(n):
    value = int(input(f"Число {i + 1}: "))
    total += value
    if value > 0:
        positive_count += 1
    if maximum is None or value > maximum:
        maximum = value

print(f"Сумма: {total}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {maximum}")