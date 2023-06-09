# Generated by Django 3.1.4 on 2022-03-10 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20220308_1902'),
        ('freelance', '0016_auto_20220308_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fcontact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('budget', models.IntegerField(max_length=20)),
                ('contact_no', models.IntegerField(max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
        ),
    ]
