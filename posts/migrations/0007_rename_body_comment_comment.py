# Generated by Django 3.2 on 2022-06-09 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_neighbor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
