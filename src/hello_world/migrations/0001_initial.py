# Generated by Django 3.1.2 on 2020-10-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aut_book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, verbose_name='Авторы книг')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Биография автора')),
            ],
        ),
    ]
