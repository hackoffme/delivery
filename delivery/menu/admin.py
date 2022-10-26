from django.contrib import admin

from .models import Categories, Products, Price


class PriceInline(admin.StackedInline):
    model = Price
    extra = 1
    prepopulated_fields = {'slug': ('product','size')}


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ['category', 'name', 'aviable']
    list_display_links = ('category', 'name')
    list_editable = ('aviable', )

    prepopulated_fields = {'slug': ('name',)}
    inlines = [PriceInline]


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'emoji')
    list_display_links = ('name', )

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Price)
class AdminPrice(admin.ModelAdmin):
    list_display = ('product', 'size', 'price', )
    list_display_links = ('product', 'size',)
    list_editable = ('price', )
    prepopulated_fields = {'slug': ('product', 'size')}
