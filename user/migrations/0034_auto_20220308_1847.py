# Generated by Django 3.1.4 on 2022-03-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0033_auto_20220308_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
