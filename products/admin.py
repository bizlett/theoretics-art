from django.contrib import admin
from .models import Category, Product, ProductVariation


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)


class ProductVariationAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'price',
        'size',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(ProductVariation, ProductVariationAdmin)
