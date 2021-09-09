from django.urls import path

from . import views

urlpatterns = [
    path('livros/', views.BookListView.as_view())
]