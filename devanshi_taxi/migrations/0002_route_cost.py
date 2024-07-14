# Generated by Django 4.2.11 on 2024-07-14 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devanshi_taxi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup', models.CharField(max_length=255)),
                ('drop', models.CharField(max_length=255)),
                ('distance', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra_fare', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devanshi_taxi.car')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devanshi_taxi.route')),
            ],
        ),
    ]
