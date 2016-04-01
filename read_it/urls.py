from django.conf.urls import url
from django.contrib import admin
from books.views import AuthorDetail, AuthorList, BookDetail, list_books, review_book, ReviewList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_books, name='books'),
    # CBVs need as_view()
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    # Class Based View
    url(r'^review/$', ReviewList.as_view(), name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
]
