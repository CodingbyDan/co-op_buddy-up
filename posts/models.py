from django.db import models
from django.contrib.auth.models import User

PLAYSTYLE_CHOICES = (
    ('relaxed', 'RELAXED'),
    ('regular', 'REGULAR'),
    ('competitive', 'COMPETITIVE')
)

PLATFORM_CHOICES = (
    ('playstation', 'PLAYSTATION'),
    ('xbox', 'XBOX'),
    ('nintendo', 'NINTENDO'),
    ('pc', 'PC')
)

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75, unique=True)
    body = models.TextField()
    platform = models.CharField(max_length=11, choices=PLATFORM_CHOICES, default='pc')
    playstyle = models.CharField(max_length=11, choices=PLAYSTYLE_CHOICES, default='relaxed')
    slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name="cobu_posts"
    # )
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
    