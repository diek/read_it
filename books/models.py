from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=70, help_text='Use pen name, not real name.')
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    is_favorite = models.BooleanField(default=False, verbose_name='Favourite?')

    def __str__(self):
        return "Author: {}, Title: {}".format(self.author, self.title)
