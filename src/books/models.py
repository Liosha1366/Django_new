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
    # author = models.CharField(
    #     'Имя автора',
    #     max_length=50,
    #     blank=False,
    #     null=False,
    # )


class Aut_book(models.Model): 
    author = models.CharField(
        'Имя автора',
        max_length=50,
        blank=False,
        null=False,
    )


class Seris(models.Model): 
    number = models.CharField(
        'Название книги',
        max_length=50,
        blank=True,
        null=True
    )
    number_type = models.ForeignKey(
        Aut_book,
        verbose_name="Автор",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.number} {self.number_type.author}'


class Genre(models.Model):
    gener = models.CharField(
        "Жанр",
        max_length=50,
        blank=False,
        null=False
    )
    number_type = models.ForeignKey(
        Seris,
        verbose_name="Название книги",
        on_delete=models.PROTECT
    )
    def __str__(self):
        return f'{self.gener} {self.number_type.number}'
    

    # books = models.ManyToManyField(
    #     'hello_world.Seris',
    #     verbose_name="Серия и Автор книги",
    #     blank=False,
    # )
    # gener = models.ManyToManyField(
    #     verbose_name="Жанр",
    #     max_length=50,
    #     blank=False,
    #     null=False
    # )
    coin = models.IntegerField(
        verbose_name="Цена книги",
        
    )
    publication_date = models.DateField(verbose_name="Дата",)
    

    def __str__(self):
        return self.name








