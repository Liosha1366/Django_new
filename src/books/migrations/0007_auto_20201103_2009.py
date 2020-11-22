# Generated by Django 3.1.2 on 2020-11-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20201103_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='number_book',
            new_name='name_book',
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Имя автора'),
        ),
    ]