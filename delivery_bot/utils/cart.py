

class Cart:
    def __init__(self, reader) -> None:
        self.items = {}
        self.price = {}
        self.reader = reader

    def add(self, key, price=0):
        self.items[key] = (self.items.get(key, None) or 0) + 1
        self.price[key] = price
        return self.items[key]

    def remove(self, key):
        self.items[key] = (self.items.get(key, None) or 0) - 1
        if self.items[key] <= 0:
            self.items.pop(key)
            return 0
        return self.items[key]

    def get_total(self):
        total = 0
        for key, count in self.items.items():
            total += count*self.price[key]
        return total

    def clear(self):
        self.items = {}

    def view(self):
        ret = 'В корзине:'
        for item, count in self.items.items():
            product = self.reader.call_retrieveProducts(
                parameters={'id': item[0]})
            size = filter(lambda x: x.id == item[1], product.price).__next__()
            ret = f'{ret}\n{product.name} {size.size}.<code> кол-во: {count} x цена: {size.price} = {count*size.price}</code>'
        ret = f'{ret}\n <code>Итоговая сумма: {self.get_total()}</code>'
        return ret

    def data_for_send(self):
        return [{'item': key[1], 'quantity': value} for key, value in self.items.items()]


{
    "customer": 3,
    "items": [{"item": 1, "quantity": 2}]
}
