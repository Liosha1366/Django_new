from django.db import models

from django.contrib.auth import get_user_model

from random import randint 
# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='carts',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(
        "Created date",
        auto_now=False,
        auto_now_add=True,
    )

    def total_price(self):
        price = 0
        for book_in_cart in self.books.all():
            price += book_in_cart.price
        return price

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        related_name='books_in_carts'
    )
    quantity = models.IntegerField(
        "Quantity",
        default=1
    )
    price = models.DecimalField(
        "Price",
        decimal_places=2,
        max_digits=5
    )

    def __str__(self) -> str:
        return f"{self.book.name_book} in cart for {self.cart.customer.username}"
    def construct_prise(self):
        self.quantity * randint(25, 250)
        