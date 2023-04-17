from django.contrib import admin

# from .forms import MenuItemsForm
from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    ordering = ("parent__position", "parent__pk")


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)
    model = Menu
    inlines = (MenuItemInline,)
