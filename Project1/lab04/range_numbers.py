a = int(input("Первое число: "))
b = int(input("Второе число: "))

if a < b:
    for x in range(a, b + 1):
        print(x)
elif a > b:
    for x in range(a, b - 1, -1):
        print(x)
else:
    print(a)