# Generated by Django 3.1.4 on 2022-02-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20220221_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Merch', 'merch'), ('Book', 'book')], default='book', max_length=10),
        ),
    ]
