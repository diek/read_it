from django.conf.urls import url
from django.contrib import admin
from books.views import list_books

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_books, name='books'),
]
