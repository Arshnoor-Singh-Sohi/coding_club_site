
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Publisher, Book, Member, Order

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'website')
    list_filter = ('country',)
    search_fields = ('name', 'city')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publisher', 'price')
    list_filter = ('category', 'publisher')
    search_fields = ('title',)
    ordering = ('title',)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'status', 'city')

admin.site.register(Member, MemberAdmin)

admin.site.register(Order)