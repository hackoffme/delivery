from rest_framework import serializers

from order import models
from utils.tg_send import send_mess


class CustomerTgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomersTg
        fields = '__all__'


class OrderCreateItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItems
        fields = ['item', 'quantity']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderCreateItemSerializer(many=True)
    customer = serializers.SlugRelatedField(
        slug_field='tg_id', queryset=models.CustomersTg.objects.all())

    class Meta:
        model = models.Orders
        fields = ['customer', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = models.Orders.objects.create(**validated_data)
        for item in items_data:
            models.OrderItems.objects.create(order=order, **item)
        send_mess(order.view())

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
