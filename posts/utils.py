from random import randint
from .models import Posts
from faker import Faker

def fake_posts(n: 10):
    fak = Faker("pl_PL")
    for _ in range(n):
        created = fak.date_time()
        post = Posts(
            title = fak.text(randint(10,30)),
            content = fak.text(randint(100,300)),
            published = fak.boolean(),
            created = created,
            modified = created + fak.time_delta(5),
            sponsored = fak.boolean()
        )
        post.save()