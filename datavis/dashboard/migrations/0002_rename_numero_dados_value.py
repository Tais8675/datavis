# Generated by Django 4.1.7 on 2023-05-11 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dados',
            old_name='numero',
            new_name='value',
        ),
    ]
