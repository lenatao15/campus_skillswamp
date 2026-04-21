from django.contrib import admin
from .models import Category, Skill

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'price', 'is_free', 'is_available', 'created_at')
    list_filter = ('is_available', 'is_free', 'category', 'created_at')
    search_fields = ('title', 'description')
