# Generated by Django 3.2 on 2022-06-09 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businesses', '0002_auto_20220609_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='owner',
            new_name='user',
        ),
    ]