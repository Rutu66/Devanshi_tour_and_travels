# Generated by Django 4.1.13 on 2024-07-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devanshi_taxi', '0003_rename_pickup_address_booking_pickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='drop',
            field=models.CharField(default='amreli', max_length=255),
            preserve_default=False,
        ),
    ]
