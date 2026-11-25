from django.contrib import admin
from .models import Meme, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'category', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('year', 'category')