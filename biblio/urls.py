from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.BookListView.as_view(), name='livros'),
    path('livros/<int:id>', views.BookDetailView.as_view(), name='detalhes')
]