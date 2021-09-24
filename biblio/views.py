from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView
from asgiref.sync import sync_to_async, async_to_sync
from django.views.generic.dates import timezone_today


from .models import Book, BookInstance, Author, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'biblio/index.html', context=context)

class BookListView(ListView):
    model = Book
    queryset = Book.objects.all()
    context_object_name = 'book_list'
    template_name = 'biblio/book-list.html'


class BookDetailView(DetailView):
    model = Book


class IndexView(TemplateView):
    template_name = 'biblio/base.html'