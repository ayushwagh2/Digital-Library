# Generated by Django 4.1.2 on 2022-12-08 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_document_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(null=True, upload_to='')),
                ('Post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
