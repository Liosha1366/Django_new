from django.db import models

# Create your models here.

class Aut_book(models.Model): 
    author = models.CharField(
        'Авторы книг',
        max_length=20,
        blank=False,
        null=False
    )
    description = models.TextField(
        'Биография автора',
        max_length=100,
        blank=True,
        null=True
    )
    def __str__(self):
        return self.author


