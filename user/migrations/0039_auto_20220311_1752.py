# Generated by Django 3.1.4 on 2022-03-11 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0038_auto_20220311_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail'),
        ),
    ]