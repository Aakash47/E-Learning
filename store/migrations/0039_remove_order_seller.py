# Generated by Django 3.1.4 on 2022-03-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0038_order_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
    ]