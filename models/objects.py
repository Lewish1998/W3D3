from models.order import *


order_1 = Order(customer_name='Jim', order_date='5/01/2023', quantity=2, item='Banana')
order_2 = Order(customer_name='Steve', order_date='3/01/2023', quantity=5, item='Apple')
order_3 = Order(customer_name='Mary', order_date='3/01/2023', quantity=15, item='Pear')
order_4 = Order(customer_name='Alice', order_date='1/01/2023', quantity=7, item='Bread')
order_5 = Order(customer_name='John', order_date='9/01/2023', quantity=9, item='Milk')

orders = [order_1, order_2, order_3, order_4, order_5]
