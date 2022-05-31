from django.contrib import admin
from .models import Items, Category

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display=('name','brand','letter_size', 'number_size', 'category','price', 'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['category']
 
