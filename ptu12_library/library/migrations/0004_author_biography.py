# Generated by Django 4.2.1 on 2023-05-31 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, max_length=8000, null=True, verbose_name='biography'),
        ),
    ]
