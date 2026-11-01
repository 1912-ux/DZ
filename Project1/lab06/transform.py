parts = input("Целые числа через пробел: ").split()
numbers = [int(p) for p in parts]
new_numbers = []
for number in numbers:
    if number < 0:
        new_numbers.append(-number)
    else:
        new_numbers.append(number)
print(f"Исходный список: {numbers}")
print(f"Новый список: {new_numbers}")