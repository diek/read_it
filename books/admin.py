from django.contrib import admin
from .models import Author, Book


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Book Details', {'fields': ['title', 'authors']}),
        ('Review', {'fields': ['is_favorite', 'review', 'date_reviewed']}),
    ]


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
