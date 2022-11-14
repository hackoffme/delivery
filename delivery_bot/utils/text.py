hi = """🍕«1:0» — это семейная пиццерия, где вы найдете широкий выбор итальянских и римских пицц, а также множество других вкусных блюд.

<b>Мы работаем с 10:00 до 22:00.</b>

Доставка:

✅ По новому городу – 140 ₽
✅ В поселок Лесной, 16-й микрорайон, Причал, КОС – 190 ₽

<b>При заказе от 700 ₽ привезем бесплатно!</b>
<i>Инструкция:
настоящие мужики хелпы не читают. Для перезапуска бота нажмите /start</i>
Самовывоз с ул. Мира 21
С любовью, пиццерия «1:0» ❤️"""


def split_text(text: str, l=4000):
    if len(text) <= l:
        return [text]
    ret = []
    text = text.split('\n')
    message = ''
    for item in text:
        if len(message)+len(item) >= l:
            ret.append(message)
            message = ''
        message += f'{item}\n'
    message and ret.append(message)
    return ret