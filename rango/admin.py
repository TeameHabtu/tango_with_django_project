from django.contrib import admin
from rango.models import Category, Page,UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'url', 'views']
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
