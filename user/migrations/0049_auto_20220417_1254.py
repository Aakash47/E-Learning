# Generated by Django 3.1.4 on 2022-04-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0048_auto_20220416_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]
