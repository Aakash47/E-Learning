# Generated by Django 3.1.4 on 2022-02-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('womens', 'Womens'), ('mens', 'Mens')], default='mens', max_length=10),
        ),
    ]