from datetime import datetime
def order_to_text(order):
    total=0
    text_item=''
    for item in order.items:
        quantity = item.quantity
        price = item.price
        text_item+=f'{item.item.product.name} {item.item.size} кол-во:{quantity} цена:{price}\n'
        total += quantity*float(price)
    ret=f'<b>Заказ</b> от {datetime.strptime(order.created, "%Y-%m-%dT%H:%M:%S.%fZ").date()}\n'\
        f'<b>Доставка по адресу:</b> {order.customer.address}\n'\
        f'<b>Меню:</b> \n'\
        f'{text_item}'\
        f'<b>Итого {total}</b>'
        
    return ret
        
    