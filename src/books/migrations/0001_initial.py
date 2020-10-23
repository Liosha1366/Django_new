# Generated by Django 3.1.2 on 2020-10-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hello_world', '0006_auto_20201023_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Издательство')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Адрес')),
                ('city', models.CharField(blank=True, max_length=60, null=True, verbose_name='Город')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Страна')),
                ('books', models.ManyToManyField(to='hello_world.Seris', verbose_name='Название книги')),
            ],
        ),
    ]