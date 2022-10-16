from .models import Book
from faker import Faker
from random import randint

def fake_books(n=10):
    fake = Faker("pl_PL")
    for _ in range(n):
        book = Book(
            title = fake.text(10),
            author = fake.name(),
            description = fake.text(randint(50,100)),
            available = fake.boolean(),
            publication_year = randint(1800,2022)
        )
        book.save()