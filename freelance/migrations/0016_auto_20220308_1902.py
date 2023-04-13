# Generated by Django 3.1.4 on 2022-03-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0015_freelance_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelance',
            name='slug',
            field=models.SlugField(help_text='This field should be unique', max_length=200, unique=True),
        ),
    ]
