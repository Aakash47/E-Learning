# Generated by Django 3.1.4 on 2022-04-16 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_auto_20220314_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.shippingaddress'),
        ),
    ]
