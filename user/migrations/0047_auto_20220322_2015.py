# Generated by Django 3.1.4 on 2022-03-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0046_auto_20220314_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='draft', max_length=10),
        ),
    ]
