from django.contrib import admin
from .models import Category, Post

# For Configuration Of Category ADmin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','url','add_date')
    search_fields = ('title','cat_id',)
    list_per_page = 10

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','cat',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
