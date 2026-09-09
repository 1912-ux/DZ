total_volume = int(input("Сколько у вас есть бутылок светлого нефильтрованного сока? "))
capacity = int(input("Введите сколько бутылок вашего СОКА, могут поместиться в 1 ящик: "))

full = total_volume / capacity
ost = total_volume % capacity

min_units = (total_volume + capacity - 1) // capacity

print("\n")
print(f"Полностью заполненных единиц: {full}")
print(f"Остаток: {ost}")
print(f"Минимальное число единиц: {min_units}")