# Generated by Django 3.1.4 on 2022-02-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20220221_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]
