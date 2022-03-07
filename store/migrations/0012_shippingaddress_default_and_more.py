# Generated by Django 4.0.2 on 2022-03-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_orderitem_complete_orderitem_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='payment_option',
            field=models.CharField(choices=[('S', 'Stripe'), ('P', 'Paypal')], default='P', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='save_info',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='use_default',
            field=models.BooleanField(default=False),
        ),
    ]
