from django.db import models
# Create your models here.

class Book(models.Model):
    name = models.CharField(
        "Издательство",
        max_length=50,
        blank=False,
        null=False,
    )

    address = models.CharField(
        "Адрес",
        max_length=50,
        blank=True,
        null=True,
    )

    city = models.CharField(
        "Город",
        max_length=60,
        blank=True,
        null=True,
    )

    country = models.CharField(
        "Страна",
        max_length=50,
        blank=True,
        null=True,
    )

    author = models.CharField(
        'Имя автора',
        default='NONE',
        max_length=50,
        blank=False,
        null=False,
    )

    number = models.CharField(
        'Название книги',
        default='NONE',
        max_length=50,
        blank=False,
        null=False,
    )

    gener = models.CharField(
        "Жанр",
        default='NONE',
        max_length=50,
        blank=False,
        null=False,
    )

    coin = models.IntegerField(
        verbose_name="Цена книги",
        default=0.0,
    )

    publication_date = models.DateField(verbose_name="Дата",)
        
    

    def __str__(self):
        return self.name








