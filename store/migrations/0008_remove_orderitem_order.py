# Generated by Django 4.0.2 on 2022-03-02 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]
