# Generated by Django 5.0.4 on 2024-04-17 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='last_name',
        ),
    ]
