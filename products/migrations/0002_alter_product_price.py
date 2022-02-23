# Generated by Django 4.0.2 on 2022-02-23 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=10, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
