import random
from datetime import datetime

from django.core.management.base import BaseCommand
from books.models import Book, Author, Genre


class Command(BaseCommand):
    help = 'Fill DB with default data'

    def handle(self, *args, **options):
        genres = Genre.objects.all()
        for i in range(1, 11):
            Author.objects.create(
                first_name=f'Name {i}',
                last_name=f'Surname {i}',
                date_of_birth=datetime(year=2000 - random.randint(1, 30), month=1, day=1 + i),
            )
        authors = Author.objects.all()
        for i in range(100):
            Book.objects.create(
                title=f'Book {i}',
                is_published=random.choice((True, False)),
                author=random.choice(authors),
                genre=random.choice(genres),
                price=random.randint(100, 900),
                rating=random.randint(1, 10)
            )

        self.stdout.write(self.style.SUCCESS('DB successfully filled'))
