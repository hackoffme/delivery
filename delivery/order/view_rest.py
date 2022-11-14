from rest_framework import viewsets, generics, exceptions
from order import models
from order import serializers


class CustomerViewDetail(viewsets.mixins.RetrieveModelMixin,
                         viewsets.mixins.CreateModelMixin,
                         viewsets.mixins.UpdateModelMixin,
                         viewsets.GenericViewSet):
    queryset = models.CustomersTg
    serializer_class = serializers.CustomerTgSerializer
    lookup_field = 'tg_id'


class OrderCreate(generics.CreateAPIView):
    queryset = models.Orders
    serializer_class = serializers.OrderCreateSerializer


class OrderViewList(viewsets.mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    lookup_url_kwarg = 'tg_id'
    serializer_class = serializers.OrderViewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        if self.lookup_url_kwarg not in self.kwargs:
            raise exceptions.NotFound
        tg_id = self.kwargs[self.lookup_url_kwarg]
        tg_id = self.kwargs['tg_id']
        ret = models.Orders.objects.filter(
            customer__tg_id=tg_id).all().order_by('-id')[:5]
        return ret
