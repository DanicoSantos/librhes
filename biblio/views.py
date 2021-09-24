from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from asgiref.sync import sync_to_async, async_to_sync
from django.views.generic.dates import timezone_today


from .models import Book

class BookListView(ListView):
    model = Book
    # queryset = Book.objects.all()
    template_name = 'biblio/book-list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class BookDetailView(DetailView):
    queryset = Book.objects.all()

    def get_queryset(self, id): 
        return Book.objects.filter(id=id)


class IndexView(TemplateView):
    template_name = 'biblio/base.html'