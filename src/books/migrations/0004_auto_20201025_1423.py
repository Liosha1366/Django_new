# Generated by Django 3.1.2 on 2020-10-25 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20201025_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='number_type',
        ),
        migrations.RemoveField(
            model_name='seris',
            name='number_type',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='NONE', max_length=50, verbose_name='Имя автора'),
        ),
        migrations.AddField(
            model_name='book',
            name='coin',
            field=models.IntegerField(default=0.0, verbose_name='Цена книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='gener',
            field=models.CharField(default='NONE', max_length=50, verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.CharField(default='NONE', max_length=50, verbose_name='Название книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Aut_book',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Seris',
        ),
    ]
