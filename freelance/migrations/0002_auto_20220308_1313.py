# Generated by Django 3.1.4 on 2022-03-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelance',
            name='Projects_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='freelance',
            name='projects_done',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
