from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from asgiref.sync import sync_to_async, async_to_sync


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


class IndexView(TemplateView):
    template_name = 'biblio/base.html'