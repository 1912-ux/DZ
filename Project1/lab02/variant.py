total_volume = int(input("Сколько у вас есть бутылок светлого нефильтрованного сока? "))
capacity = int(input("Введите сколько бутылок вашего СОКА, могут поместиться в 1 ящик: "))

full_buses = total_volume // capacity
remainder = total_volume % capacity
buses_needed = (total_volume + capacity - 1) // capacity

print()
print(f"Полностью заполненных автобусов: {full_buses}")
print(f"Остаток студентов: {remainder}")
print(f"Минимально нужно автобусов: {buses_needed}")