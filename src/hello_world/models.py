from django.db import models

# Create your models here.



class Public(models.Model):
    name = models.CharField(
        "Издательство",
        max_length=50,
        blank=False,
        null=False
    )
    books = models.ManyToManyField(
        'hello_world.Seris',
        verbose_name="Название книги"
    )
    def __str__(self):
        return self.name


class Genre(models.Model):
    gener_tab = models.CharField(
        "Жанр",
        max_length=50,
        blank=False,
        null=False
    )
    number_type = models.ForeignKey(
        Public,
        verbose_name="Книги",
        on_delete=models.PROTECT
    )
    def __str__(self):
        return f'{self.gener_tab} {self.number_type.name}'


class Aut_book(models.Model): 
    author = models.CharField(
        'Авторы книг',
        max_length=50,
        blank=False,
        null=False
    )
    description = models.TextField(
        'Биография автора',
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author


class Seris(models.Model): 
    number = models.CharField(
        'Серия книги',
        max_length=50,
        blank=False,
        null=False
    )
    number_type = models.ForeignKey(
        Aut_book,
        verbose_name="Автор",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.number} {self.number_type.author}'