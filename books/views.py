from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "category", "published_date"]
    success_url = reverse_lazy("book_list")

class BookUpdateView(UpdateView): 
        model = Book
        fields = ["title", "author", "category", "published_date"]
        success_url = reverse_lazy("book_list")

class BookDeleteView(DeleteView): 
     model= Book
     success_url = reverse_lazy("book_list")