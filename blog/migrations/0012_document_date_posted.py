# Generated by Django 4.1.2 on 2022-12-08 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_document_post_remove_document_document2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]