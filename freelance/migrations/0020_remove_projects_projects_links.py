# Generated by Django 3.1.4 on 2022-03-14 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0019_fcontact_freelance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='Projects_links',
        ),
    ]
