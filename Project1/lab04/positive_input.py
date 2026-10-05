attempts = 0
value = int(input("Введите целое число: "))

while value <= 0:
    attempts += 1
    value = int(input("Нужно положительное. Ещё раз: "))

print(f"Квадрат: {value ** 2}")
print(f"Отклонено попыток: {attempts}")