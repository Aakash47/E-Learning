# Generated by Django 3.1.4 on 2022-03-08 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20220308_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('merch', 'Merch'), ('book', 'Book')], default='book', max_length=10),
        ),
    ]
