from django.contrib import admin
from .models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Book Details', {'fields': ['title', 'authors']}),
        ('Review', {'fields': ['is_favourite', 'review', 'date_reviewed']}),
    ]

    readonly_fields = ('date_reviewed',)

    # Authors has a many to many to use the method from the obj to get the author
    def book_authors(self, obj):
        # List of authors for each obj
        return obj.list_authors()

    # Set user friendly column header
    book_authors.short_description = 'Author(s)'
    list_display = ('title', 'book_authors', 'date_reviewed', 'is_favourite',)
    list_editable = ('is_favourite', )

    # Add Sort
    list_display_links = ('title', 'date_reviewed', )

    # Add Filter
    list_filter = ('is_favourite', )

    # Search, note double __ for author
    search_fields = ('title', 'authors__name', )

admin.site.register(Author)

