year = int(input("Год (1–9999): "))

if 1 <= year <= 9999:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Да, високосный")
    else:
        print("Нет, не високосный")
else:
    print("Ошибка диапазона")