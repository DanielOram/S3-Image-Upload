# Generated by Django 3.1.5 on 2021-01-30 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestS3Upload',
            new_name='Upload',
        ),
    ]