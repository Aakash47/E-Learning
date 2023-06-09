# Generated by Django 3.1.4 on 2022-02-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20220214_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('mens', 'Mens'), ('womens', 'Womens')], default='mens', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='This field should be unique', max_length=200, unique=True),
        ),
    ]
