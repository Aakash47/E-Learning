# Generated by Django 3.1.4 on 2022-02-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20220226_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='resource',
            field=models.FileField(blank=True, null=True, upload_to='resources'),
        ),
    ]
