from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Aut_book)
admin.site.register(models.Seris)
admin.site.register(models.Publish)
admin.site.register(models.Genre)
