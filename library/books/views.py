from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import ListView, DetailView, CreateView

from books.models import Author, Book, Genre
from books.forms import BookForm


# def authors_list(request):
#     authors = Author.objects.all()
#     context = {'authors': authors, 'title': 'List of Authors'}
#     return render(request=request, template_name='books/author_list.html', context=context)

class AuthorListView(ListView):
    model = Author
    extra_context = {'title': 'List of Authors'}


class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):
        query = super().get_queryset()
        return query.select_related('author', 'genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.all()
        return context


class GenreListView(ListView):
    model = Book
    template_name = 'books/genre.html'
    context_object_name = 'books'

    def get_queryset(self):
        books = Book.objects.filter(genre__id=self.kwargs['genre_id'])
        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


# def books_list(request):
#     books = Book.objects.all()
#     genres = Genre.objects.all()
#     context = {
#         'books': books,
#         'genres': genres
#     }
#
#     return render(request=request, template_name='books/books_list.html', context=context)


# def genre_detail(request, genre_id):
#     books = Book.objects.filter(genre__id=genre_id)
#     genres = Genre.objects.all()
#     try:
#         genre = Genre.objects.get(pk=genre_id)
#     except Genre.DoesNotExist:
#         return HttpResponseNotFound()
#
#     context = {
#         'books': books,
#         'genres': genres,
#         'genre': genre
#     }
#
#     return render(request, 'books/genre.html', context)


# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             book = form.save()
#             return redirect('book_detail', book_id=book.pk)
#     else:
#         form = BookForm()
#     return render(request, 'books/create_book.html', {'form': form})


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm()
    template_name = 'books/create_book.html'

# def book_detail(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     context = {"book": book}
#     return render(request, "books/book_detail.html", context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
