from django.shortcuts import render
from .models import Book


def list_books(request):
    """
    List all the books that have reviews
    """

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books
    }

    return render(request, 'books/list.html', context)

