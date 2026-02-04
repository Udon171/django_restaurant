from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_vegetarian', 'is_vegan', 'is_available')
    list_filter = ('category', 'is_vegetarian', 'is_vegan', 'is_gluten_free', 'is_available')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_available')
