# Generated by Django 3.1.4 on 2022-03-11 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_product_seller'),
        ('courses', '0013_auto_20220301_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]
