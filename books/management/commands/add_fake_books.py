from django.core.management import BaseCommand
from books.utils import fake_books

class Command(BaseCommand):

    help = 'Creating fake books'

    def handle(self, *args, **options):
        n = options.get("number", 10)
        books = fake_books(n)
        self.stdout.write(f'{n} was created!')

    def add_arguments(self, parser):
        parser.add_argument(
            '-n','--number',type=int,
            default=10,dest="number",help="Amount of books to create"
        )