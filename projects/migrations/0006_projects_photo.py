# Generated by Django 5.0.6 on 2024-06-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_projects_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
    ]
