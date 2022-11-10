import pickle
import base64
from repositories.open_api import api_io


class Cart:
    def __init__(self, items={}, price={}) -> None:
        self.items = items or {}
        self.price = price or {}
        
    @classmethod    
    def loads(cls, data):
        if not data:
            return cls()
        return pickle.loads(base64.b64decode(data))   
    
    def dumps(self):
        return base64.b64encode(pickle.dumps(self)).decode('ascii')
        

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
            product = api_io.call_retrieveProducts(
                parameters={'id': item[0]})
            size = filter(lambda x: x.id == item[1], product.price).__next__()
            ret = f'{ret}\n{product.name} {size.size}.<code> кол-во: {count} x цена: {size.price} = {count*size.price}</code>'
        ret = f'{ret}\n <code>Итоговая сумма: {self.get_total()}</code>'
        return ret

    def data_for_send(self):
        return [{'item': key[1], 'quantity': value} for key, value in self.items.items()]

