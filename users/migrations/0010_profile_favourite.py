# Generated by Django 4.1.2 on 2022-12-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_remove_post_likes_document_likes'),
        ('users', '0009_alter_account_studentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favourite',
            field=models.ManyToManyField(to='blog.document'),
        ),
    ]
