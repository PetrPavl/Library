from django.urls import path

from .views import BookListView, AuthorListView, GenreListView, BookCreateView, BookDetailView


urlpatterns = [
    path('', BookListView.as_view(), name="books_list"),
    path('authors/', AuthorListView.as_view(), name="authors_list"),
    path('books/genres/<int:genre_id>', GenreListView.as_view(), name="genre_detail"),
    path('books/<int:pk>', BookDetailView.as_view(), name="book_detail"),
    path('books/add-book', BookCreateView.as_view(), name='add_book')
]
