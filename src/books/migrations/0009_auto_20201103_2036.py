# Generated by Django 3.1.2 on 2020-11-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20201103_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='NONE', max_length=50, verbose_name='Имя автора'),
        ),
    ]