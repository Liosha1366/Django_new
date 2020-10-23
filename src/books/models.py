from django.db import models

# Create your models here.

# class Publish(models.Model):
#     name = models.CharField(
#         "Издательство",
#         max_length=50,
#         blank=False,
#         null=False,
#     )
#     address = models.CharField(
#         "Адрес",
#         max_length=50,
#     )
#     city = models.CharField(
#         "Город",
#         max_length=60,
#     )
#     country = models.CharField(
#         "Страна",
#         max_length=50,
#     )
#     books = models.ManyToManyField(
#         'hello_world.Seris',
#         verbose_name="Название книги",
#     )

#     def __str__(self):
#         return self.name





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

