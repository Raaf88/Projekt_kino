# Generated by Django 4.0.dev20210403125743 on 2021-05-22 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mspot', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Gatunek',
        ),
        migrations.AddField(
            model_name='movie',
            name='rezyser',
            field=models.CharField(db_index=True, default='unknown', max_length=180),
        ),
        migrations.AddField(
            model_name='movie',
            name='rok_produkcji',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2030)]),
        ),
    ]