# Generated by Django 3.1.4 on 2022-03-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0042_auto_20220314_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
