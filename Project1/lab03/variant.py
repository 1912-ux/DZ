level = int(input("Заряд аккумулятора (0–100): "))

if level < 0 or level > 100:
    print("Ошибка диапазона")
elif level <= 19:
    print("Низкий")
elif level <= 79:
    print("Средний")
else:
    print("Высокий")