# Generated by Django 3.1.4 on 2021-02-12 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210212_1826'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Article',
        ),
    ]
