# Generated by Django 4.0.dev20210403125743 on 2021-05-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mspot', '0004_alter_movie_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_poster',
            field=models.ImageField(default='posters/brakobrazu.png', upload_to='movies/'),
        ),
    ]
