# Generated by Django 5.0.1 on 2024-03-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chefspecial',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='chefspecial',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]