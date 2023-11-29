from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="books/profile_images", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Author: {self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="books/covers")
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(null=True)
    rating = models.IntegerField(default=8)

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Book: {self.title} {self.author}'


class Genre(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Жанр'       # для адмінки
        verbose_name_plural = 'Жанри'
        ordering = ['title']

    def __str__(self):
        return f'Genre: {self.title}'

