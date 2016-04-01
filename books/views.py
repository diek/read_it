from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, View
from .forms import BookForm, ReviewForm
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


# Paste into Views.py - don't forget to import get_object_or_404!
# A class based view => Mapping a model to a form
class ReviewList(View):
    """
    List all of the books that we want to review.
    """
    def get(self, request):
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

        context = {
            'books': books,
            'form': BookForm,  # add the view to the context
        }

        return render(request, "books/list-to-review.html", context)

    def post(self, request):
        form = BookForm(request.POST)
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

        if form.is_valid():
            form.save()
            return redirect('review-books')

        context = {
            'form': form,
            'books': books,
        }

        return render(request, "books/list-to-review.html", context)


def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        # Process our form & Bind the request data to the form
        form = ReviewForm(request.POST)

        if form.is_valid():
            book.is_favourite = form.cleaned_data['is_favourite']
            book.review = form.cleaned_data['review']
            book.reviewed_by = request.user
            book.save()
            # pass the name of the url
            return redirect('review-books')
    else:
        form = ReviewForm

    context = {
        'book': book,
        'form': form,
    }

    return render(request, "books/review-book.html", context)
