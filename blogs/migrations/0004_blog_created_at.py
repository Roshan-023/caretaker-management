# Generated by Django 5.0.4 on 2024-04-21 14:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
