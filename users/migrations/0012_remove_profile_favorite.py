# Generated by Django 4.1.2 on 2022-12-28 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_rename_favourite_profile_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorite',
        ),
    ]
