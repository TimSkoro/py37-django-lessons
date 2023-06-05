from django.contrib import admin
from .models import *


# Register your models here.

# admin.site.register(Product)  # 1st
#
#
# class ProductAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Product, ProductAdmin)  # 2nd

@admin.action(description="Sale to 20prc")
def sale(modeladmin, request, queryset):
    queryset.update(sale_count=0.8, sale=True)


@admin.action(description="Sale Off")
def sale_off(modeladmin, request, queryset):
    queryset.update(sale_count=1, sale=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # 3rd
    list_display = ['id', 'title', 'current_price', 'created_at', 'sale']
    list_filter = ['created_at']
    search_fields = ['title']
    actions = [sale, sale_off]


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Car)
