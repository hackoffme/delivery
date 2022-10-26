from dataclasses import field
from datetime import datetime
from rest_framework import serializers

from order import models
from menu.serializers import PriceSerializers
from utils.tg_send import send_mess

class CustomerTgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomersTg
        fields = '__all__'


# class OrderItemSerializer(serializers.ModelSerializer):
#     item = PriceSerializers()

#     class Meta:
#         model = models.OrderItems
#         fields = ['item', 'quantity']


# class OrderSerializer(serializers.ModelSerializer):
#     customer = CustomerTgSerializer()
#     items = OrderItemSerializer(many=True)

#     class Meta:
#         model = models.Orders
#         fields = ['customer', 'items', 'total']

class OrderCreateItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.OrderItems
        fields = ['item', 'quantity']
    
    
class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderCreateItemSerializer(many=True)
    customer = serializers.SlugRelatedField(slug_field='tg_id', queryset=models.CustomersTg.objects.all())
    
    class Meta:
        model = models.Orders
        fields = ['customer', 'items']
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = models.Orders.objects.create(**validated_data)
        for item in items_data:
            models.OrderItems.objects.create(order=order, **item)
        # start = datetime.now()
        # asyncio.run(send_mess(order.view()))
        send_mess(order.view())
        # th = threading.Thread(target=send_mess, args=(order.view(),)).start()
        # print(datetime.now()-start, 'time')
        return order

class OrderItemsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['item', 'quantity', 'price']
        depth = 2


class OrderViewSerializer(serializers.ModelSerializer):
    items = OrderItemsViewSerializer(many=True)
    class Meta:
        model = models.Orders
        fields = ['customer', 'items', 'created', 'view']
        depth = 1