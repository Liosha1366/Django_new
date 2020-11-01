from django.db import models

# Create your models here.


class Publish(models.Model):
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

    def __str__(self):
        return self.name

    

class Aut_book(models.Model): 
    author = models.CharField(
        'Имя автора',
        default=None,
        max_length=50,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        "Фамилия автора",
        max_length=50,
        blank=True,
        null=True,
        )
    description = models.TextField(
        'Биография автора',
        max_length=500,
        blank=True,
        
    )
    
    def __str__(self):
        return self.author

    


class Seris(models.Model): 
    number = models.CharField(
        'Серия книги',
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
    gener_tab = models.CharField(
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
        return f'{self.gener_tab} {self.number_type.number}'