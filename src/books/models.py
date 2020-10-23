from django.db import models
# Create your models here.

class Publishing(models.Model):
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
    books = models.ManyToManyField(
        'hello_world.Seris',
        verbose_name="Название книги",
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name






# class Book(models.Model):
#     title = models.CharField(
#         "",
#         max_length=100,
#     )
#     authors = models.ManyToManyField(
#         Aut_book,
#         verbose_name="Автор",
#         )
#     publish = models.ForeignKey(
#         Publish,
#         verbose_name="Издательство",
#     )
#     publication_date = models.DateField()

