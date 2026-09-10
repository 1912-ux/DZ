surname = str(input("Введите фамилию:"))
name = str(input("Введите имя:"))
group = str(input("Введите группу:"))
city = str(input("Введите город:"))
age = int(input("Сколько полных лет:"))
favorite_sub = str(input("Введите любимый предмет:"))
hour = float(input("Введите количество часов подготовки в неделю:"))



print("\n")
print("Полное имя:",surname + " " + name)
print("Возраст через 4 года:", age + 4)
print("Примерное время подготовки за 4 недели: ",hour * 4)
print("Среднее время подготовки в день за семидневную неделю:",hour)

