from django.contrib import admin

from categories.models import CategoryModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title']
    search = ['title']
