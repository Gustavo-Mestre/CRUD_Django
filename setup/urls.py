from django.contrib import admin
from django.urls import path
from books.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BookListView.as_view(), name="book_list"),
    path("create", BookCreateView.as_view(), name="book_create"),
    path("update/<int:pk>", BookUpdateView.as_view(), name="book_update"),
    path("delete/<int:pk>", BookDeleteView.as_view(), name="book_delete")
]
