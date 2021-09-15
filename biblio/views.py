from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView


from .models import Book

class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'biblio/book-list.html'


class IndexView(TemplateView):
    template_name = 'biblio/base.html'