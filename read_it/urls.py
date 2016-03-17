from django.conf.urls import url
from django.contrib import admin
from books.views import AuthorDetail, AuthorList, BookDetail, list_books

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_books, name='books'),
    # CBVs need as_view()
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^authors/(?P<pk>[-\w]+)/$', AuthorDetail.as_view(), name='author-detail'),
    url(r'^books/(?P<pk>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
]
