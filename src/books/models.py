from django.db import models


# Create your models here.

def upload(inst, filename):
    print(inst, filename)
    return f'book_pics/{inst.pk}-{filename}'


class Book(models.Model):


    aut_book = models.CharField(
    'Имя автора',
         max_length=50,
         blank=False,
         null=False,
    )

    pic = models.ImageField(
        "Book_picture",
        upload_to=upload,
        blank=True,
        null=True,

    )
    
    publish = models.CharField(
        "Издательство",
        max_length=50,
        blank=False,
        null=False,
    )

    # address = models.CharField(
    #     "Адрес",
    #     max_length=50,
    #     blank=True,
    #     null=True,
    # )

    # city = models.CharField(
    #     "Город",
    #     max_length=60,
    #     blank=True,
    #     null=True,
    # )

    country = models.CharField(
        "Страна",
        max_length=50,
        blank=True,
        null=True,
    )

    name_book = models.CharField(
        'Название книги',
        default='NONE',
        max_length=50,
        blank=False,
        null=False,
    )
    pic = models.ImageField(
        "Book picture",
        upload_to=upload,
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

    created = models.DateTimeField(
        verbose_name="created",
        auto_now=False,
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name="updated",
        auto_now=True,
        auto_now_add=False,
    )
    # publication_date = models.DateField(verbose_name="Дата",)
        
    

    def __str__(self):
        return self.aut_book








