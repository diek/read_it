from django.http import HttpResponse
from django.shortcuts import render


def list_books(request):
    return HttpResponse('ReadIt App')

