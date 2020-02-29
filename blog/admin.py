from django.contrib import admin
from .models import Category, Articles
# Register your models here.

@admin.register(Articles)
class Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)
    list_filter = ('status', 'created', 'publish', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'parent',)

