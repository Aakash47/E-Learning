# Generated by Django 3.1.4 on 2022-03-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20220308_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('merch', 'Merch'), ('book', 'Book')], default='book', max_length=10),
        ),
    ]
