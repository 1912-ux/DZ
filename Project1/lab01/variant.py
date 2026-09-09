print("Добро пожаловать")

order_name = input("Введите номер заказа: ")
customer_name = input("Введите ваше имя: ")

item1_name = input("Введите название первой позиции: ")
item1_qwerty = int(input("Введите количество первой позиции: "))
item1_price = float(input("Введите цену первой позиции: "))

item2_name = input("Введите название второй позиции: ")
item2_qwerty = int(input("Введите количество второй позиции: "))
item2_price = float(input("Введите цену второй позиции: "))

delivery_cost = float(input("Введите стоимость доставки: "))
paid_amount = float(input("Введите внесённую сумму: "))

item1_cost = item1_qwerty * item1_price
item2_cost = item2_qwerty * item2_price

items_total = item1_cost + item2_cost

total_with_delivery = items_total + delivery_cost

total_qwerty = item1_qwerty + item2_qwerty

change = paid_amount - total_with_delivery

print("\n")
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")

print(f"{item1_name} | {item1_qwerty} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_qwerty} | {item2_price:.2f} | {item2_cost:.2f}")

print(f"Стоимость товаров без доставки: {items_total:.2f} руб")
print(f"Стоимость доставки: {delivery_cost:.2f} руб")
print(f"Общая сумма с доставкой: {total_with_delivery:.2f} руб")
print(f"Общее количество единиц: {total_qwerty}")
print(f"Внесённая сумма: {paid_amount:.2f} руб")
print(f"Сдача: {change:.2f} руб")

