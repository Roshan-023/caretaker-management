# Generated by Django 5.0.4 on 2024-05-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='apartment_building_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='hno',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='landmark',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='other_instructions',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='street',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
