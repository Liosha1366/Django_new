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
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author


class Seris(models.Model): 
    number = models.CharField(
        'Серия книги',
        max_length=20,
        blank=False,
        null=False
    )
    number_type = models.ForeignKey(
        Aut_book,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.number} {self.number_type.author}'