from django.db import models

# Create your models here.

class Aut_book(models.Model): 
    author = models.CharField(
        'Авторы книг',
        max_length=20,
    )
    description = models.TextField(
        'Биография автора',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author


