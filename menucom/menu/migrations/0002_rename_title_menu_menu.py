# Generated by Django 5.1.2 on 2024-12-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='title',
            new_name='menu',
        ),
    ]
