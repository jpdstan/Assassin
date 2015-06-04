from django.contrib import admin
from blog.models import Category, Page

# class CatAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'views', 'likes')
class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)