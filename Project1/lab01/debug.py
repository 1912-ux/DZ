first = "2"
second = "3"
print("Типы до:", type(first), type(second))
first = int(first)
second = int(second)
print("Типы после:", type(first), type(second))
print("Результат А:", first + second)

age = input("Возраст: ")
print("Тип до:", type(age))
age = int(age)
print("Тип после:", type(age))
print("Результат Б:", age + 1)

first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Результат В:", average)