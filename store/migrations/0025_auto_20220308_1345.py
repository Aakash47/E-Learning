# Generated by Django 3.1.4 on 2022-03-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20220308_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('book', 'Book'), ('merch', 'Merch')], default='book', max_length=10),
        ),
    ]
