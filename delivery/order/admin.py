from django.contrib import admin

from order import models


admin.site.register(models.CustomersTg)


class OrderItemsAdmin(admin.TabularInline):
    fields = ['item', 'quantity', 'price' , 'get_summ']
    readonly_fields = ['price', 'get_summ']
    model=models.OrderItems
    extra = 1
    def get_summ(self, obj):
        return obj.quantity*obj.item.price
    get_summ.short_description = 'Сумма'


@admin.register(models.Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'customer', 'total']
    list_display_links = ('customer',)
    fields = ['customer', ]
    list_per_page = 15
    
    
    inlines = [OrderItemsAdmin]
