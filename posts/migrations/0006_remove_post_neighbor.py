# Generated by Django 3.2 on 2022-06-09 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_neighbors_post_neighbor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='neighbor',
        ),
    ]
