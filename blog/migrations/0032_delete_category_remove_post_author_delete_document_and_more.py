# Generated by Django 4.1.2 on 2023-02-25 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_stream_document2_stream'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
