# Generated by Django 3.2.23 on 2024-01-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='hghhhh', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
