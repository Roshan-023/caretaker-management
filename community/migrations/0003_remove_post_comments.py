# Generated by Django 5.0.4 on 2024-04-19 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
