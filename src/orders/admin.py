from django.contrib import admin

from orders import models
# Register your models here.

admin.site.register(models.Cart)
admin.site.register(models.BookInCart)