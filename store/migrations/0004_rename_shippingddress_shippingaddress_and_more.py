# Generated by Django 4.0.2 on 2022-02-28 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_options_alter_order_customer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shippingddress',
            new_name='Shippingaddress',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='unit_price',
        ),
    ]
