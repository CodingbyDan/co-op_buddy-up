from django.db import models

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

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    platform = models.CharField(max_length=11, choices=PLATFORM_CHOICES, default='pc')
    playstyle = models.CharField(max_length=11, choices=PLAYSTYLE_CHOICES, default='relaxed')
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    