sub1 = input("Введите название первого предмета: ")
sub2 = input("Введите название второго предмета: ")
les1 = int(input(f"Введите количество занятий по предмету {sub1} за неделю: "))
les2 = int(input(f"Введите количество занятий по предмету {sub2} за неделю: "))
duration = int(input("Введите продолжительность одного занятия в минутах: "))

load1 = les1 * duration
load2 = les2 * duration
total_load_min = load1 + load2
total_load_hours = total_load_min / 60

available_time = float(input("Введите доступное время на неделю в часах: "))

if available_time < total_load_hours:
    print("Ошибка: доступное время меньше суммарной нагрузки.")
else:
    free_time = available_time - total_load_hours
    load_4_weeks_min = total_load_min * 4
    load_4_weeks_hours = total_load_hours * 4

    print()
    print(f"Нагрузка по предмету {sub1}: {load1} минут")
    print(f"Нагрузка по предмету {sub2}: {load2} минут")
    print(f"Общая нагрузка: {total_load_min} минут {total_load_hours:.2f} часов")
    print(f"Остаток свободного времени: {free_time:.2f} часов")
    print(f"Нагрузка за 4 недели: {load_4_weeks_min} минут {load_4_weeks_hours:.2f} часов")