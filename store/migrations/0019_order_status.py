# Generated by Django 4.0.2 on 2022-03-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False, max_length=1, null=True),
        ),
    ]
