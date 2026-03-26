import json
from datetime import datetime
with open(r'F:\Projects\Scillfactory\Bedt\orders_july_2023.json', 'r') as orders_file:
    orders = json.load(orders_file)
max_price = 0
total_price = 0
max_quantity = 0
total_quantity = 0
max_order = ''
max_quantity_order = ''
total_orders_count = len(orders)
daily_orders_count = {}
user_orders_count = {}
summary_price = {}



for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    date = orders_data['date']
    user_id = orders_data['user_id']
    total_cost = price * quantity
    if price > max_price:
        max_order = order_num
        max_price = price
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order = order_num
    daily_orders_count[date] = daily_orders_count.get(date, 0) + 1
    user_orders_count[user_id] = user_orders_count.get(user_id, 0) + 1
    summary_price[user_id] = summary_price.get(user_id, 0) + total_cost
    total_price += price
    total_quantity += quantity
    medium_order_price = float((total_price) / (total_orders_count))
    medium_unit_price = float((total_price) / (total_quantity))
print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price:.2f}')
print(f'2. Номер заказа с самым большим количеством товаров ({max_quantity}): {max_quantity_order}')
best_day = max(daily_orders_count, key=daily_orders_count.get)
formatted_day = datetime.strptime(best_day, '%Y-%m-%d').strftime('%d')
print(f'3. {formatted_day} июля было продано больше всего товаров: {daily_orders_count[best_day]}')
leader_id = max(user_orders_count, key=user_orders_count.get)
print(f'4. Покупатель №{leader_id} сделал больше всего заказов: {user_orders_count[leader_id]}')
best_cust_id = max(summary_price, key=summary_price.get)
print(f'5. Покупатель №{best_cust_id} принес больше всего денег: {summary_price[best_cust_id]:.2f}')
print(f'6. Cредняя стоимость заказа в июле cоставила {medium_order_price:.2f}')
print(f'7. Средняя стоимость товаров в июле составила {medium_unit_price:.2f}')