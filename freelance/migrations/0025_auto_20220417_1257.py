# Generated by Django 3.1.4 on 2022-04-17 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0024_auto_20220417_1254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcontact',
            options={},
        ),
        migrations.RemoveField(
            model_name='fcontact',
            name='date_contacted',
        ),
    ]
