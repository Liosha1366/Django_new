# Generated by Django 3.1.2 on 2020-11-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0008_auto_20201025_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aut_book',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия автора'),
        ),
    ]
