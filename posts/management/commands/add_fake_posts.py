from django.core.management import BaseCommand
from posts.utils import fake_posts


class Command(BaseCommand):

    help = 'Creating random posts'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--number',
            type=int, default=10, dest='number',
            help= 'Amount of posts'
        )

    def handle(self, *args, **options):
        n = options.get("number",10)
        fake_posts(n)
        self.stdout.write(f'{n} posts has been created')
