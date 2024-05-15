# Generated by Django 5.0.4 on 2024-05-12 07:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_is_recurring_field_booking_is_recurring'),
        ('myNannyApplication', '0004_rename_dmn_about_domain_domin_about'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RateNanny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(blank=True, max_length=60, null=True)),
                ('content', models.CharField(blank=True, max_length=60, null=True)),
                ('rating', models.PositiveIntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myNannyApplication.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]