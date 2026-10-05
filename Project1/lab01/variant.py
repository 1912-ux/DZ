order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

item1 = input("Название первой позиции: ")
qty1 = int(input(f"Количество «{item1}»: "))
price1 = float(input(f"Цена за единицу «{item1}» (руб.): "))

item2 = input("Название второй позиции: ")
qty2 = int(input(f"Количество «{item2}»: "))
price2 = float(input(f"Цена за единицу «{item2}» (руб.): "))

delivery = float(input("Стоимость доставки (руб.): "))
paid = float(input("Внесённая сумма (руб.): "))

cost1 = qty1 * price1
cost2 = qty2 * price2
goods_total = cost1 + cost2
grand_total = goods_total + delivery
total_qty = qty1 + qty2
change = paid - grand_total

print()
print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer}")
print(f"{item1} | {qty1} | {price1:.2f} | {cost1:.2f}")
print(f"{item2} | {qty2} | {price2:.2f} | {cost2:.2f}")
print(f"Стоимость товаров без доставки: {goods_total:.2f} руб.")
print(f"Доставка: {delivery:.2f} руб.")
print(f"Итоговая сумма с доставкой: {grand_total:.2f} руб.")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f} руб.")