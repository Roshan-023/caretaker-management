# Generated by Django 5.0.4 on 2024-05-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=None, upload_to='media/blogs'),
        ),
    ]