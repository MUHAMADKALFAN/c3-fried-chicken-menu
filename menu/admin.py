from django.contrib import admin
from .models import Category, MenuItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "active")
    list_editable = ("order", "active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "available", "featured", "order")
    list_filter = ("category", "available", "featured")
    list_editable = ("price", "available", "featured", "order")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
