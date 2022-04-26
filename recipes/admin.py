from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category',)
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
