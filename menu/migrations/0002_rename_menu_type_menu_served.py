# Generated by Django 5.0.1 on 2024-03-11 16:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_type',
            new_name='served',
        ),
    ]
