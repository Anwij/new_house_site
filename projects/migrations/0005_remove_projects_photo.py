# Generated by Django 5.0.6 on 2024-06-18 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_projects_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='photo',
        ),
    ]
