from django.contrib import admin
from .models import Publisher, Book

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'website')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publisher', 'price')
    list_filter = ('category', 'publisher')
    search_fields = ('title',)
