# Generated by Django 3.1.4 on 2022-03-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20220307_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('merch', 'Merch'), ('book', 'Book')], default='book', max_length=10),
        ),
    ]
