# Generated by Django 3.1.4 on 2022-02-21 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Book', 'book'), ('Merch', 'merch')], default='book', max_length=10),
        ),
    ]