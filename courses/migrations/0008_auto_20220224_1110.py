# Generated by Django 3.1.4 on 2022-02-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(help_text='This field should be unique', max_length=100, unique=True),
        ),
    ]
