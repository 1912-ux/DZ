a = float(input("Первое число: "))
b = float(input("Второе число: "))
op = input("Операция (+ - * /): ")

if op == "+":
    result = a + b
    print(f"Результат: {result:.2f}")
elif op == "-":
    result = a - b
    print(f"Результат: {result:.2f}")
elif op == "*":
    result = a * b
    print(f"Результат: {result:.2f}")
elif op == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        result = a / b
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")