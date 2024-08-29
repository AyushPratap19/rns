from django.contrib import admin
from .models import Product, Category, Brand, ProductImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'condition', 'category', 'brand', 'price', 'created')
    search_fields = ('name', 'description', 'condition', 'category__category_name', 'brand__brand_name')
    list_filter = ('condition', 'category', 'brand')
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate the slug from the name

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)

@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
