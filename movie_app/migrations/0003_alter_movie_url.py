# Generated by Django 5.0 on 2023-12-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
