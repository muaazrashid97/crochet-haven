from django.contrib import admin
from .models import Product
from django.utils.html import format_html

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'preview_image')
    readonly_fields = ('preview_image',)
    fields = ('name', 'price', 'description', 'image', 'preview_image')

    def preview_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="height: 100px; object-fit: cover; border-radius: 4px; box-shadow: 0 0 5px #ccc;" />',
    obj.image.url)
        return "No image"

    preview_image.short_description = "Image Preview"
