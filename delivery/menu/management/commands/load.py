import json
import os
from random import randint
from pytils.translit import slugify

from django.core.management.base import BaseCommand


from menu import models

def load_json():
    with open('./data/data.txt', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data
        

class Command(BaseCommand):
    help = 'load data from old site'
    
    def handle(self, *args, **options):
        data = load_json()
        for item in data:
            cat = models.Categories.objects.create(name=item['cat'], emoji=item['emoji'], slug=slugify(item['cat']))
            for menu in item['menu']:
                product = models.Products.objects.filter(name=menu['name']).first()
                
                if product:
                    price = models.Price.objects.create(size=menu['subcategory'], 
                                                        price=menu['price'], 
                                                        product=product,
                                                        slug=slugify(f"{cat.name}-{m.name}-{menu['subcategory']}"))
                    continue

                if menu['image']:
                    img = os.path.splitext(menu['image'])[0]+'.webp'
                    image =  f"old/{img}"
                else:
                    image = None
                
                
                m = models.Products(
                    name=menu['name'],
                    slug=slugify(menu['name']+menu['subcategory'].__str__()),
                    category=cat,
                    description=menu['description'],
                    image=image,
                )
                m.save()
                price = models.Price.objects.create(size=menu['subcategory'], price=menu['price'], product=m, 
                                                    slug=slugify(f"{cat.name}-{m.name}-{menu['subcategory']}"))
                price.save()
                
