# Generated by Django 3.1.4 on 2022-04-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_auto_20220417_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('merch', 'Merch'), ('book', 'Book')], default='book', max_length=10),
        ),
    ]
