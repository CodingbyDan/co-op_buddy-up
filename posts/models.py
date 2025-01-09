from django.db import models
from django.contrib.auth.models import User
import uuid

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author : {self.body[30]}'