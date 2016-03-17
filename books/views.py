from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Author, Book


def list_books(request):
    """
    List all the books that have reviews
    """

    # use prefetch_related, the authors, and just reference it, vice query the db very time.
    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books
    }

    return render(request, 'books/list.html', context)


# Class Based View
class AuthorList(View):
    def get(self, request):

        # authors = Author.objects.all()
        authors = Author.objects.annotate(
            published_books=Count('books')).filter(
                # count > 0, note the double underscore
                published_books__gt=0)

        context = {
            'authors': authors
        }

        return render(request, 'books/authors.html', context)


# Class Based View - Generic
class BookDetail(DetailView):
    model = Book
    template_name = 'books/book.html'


class AuthorDetail(DetailView):
    model = Author
    template_name = 'books/author.html'

