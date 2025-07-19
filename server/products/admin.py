from django.contrib import admin
from .models import Category, Product, ProductImage

admin.site.register(Category)

# Register Product and his Photo
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]