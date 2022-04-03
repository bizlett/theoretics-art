from django.contrib import admin
from .models import Category, Product, Art, Photography


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'image',
    )


class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'dimensions',
        'price',
    )


class PhotographyAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'size',
        'price',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Art, ArtAdmin)
admin.site.register(Photography, PhotographyAdmin)
