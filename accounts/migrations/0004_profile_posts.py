# Generated by Django 3.2 on 2022-06-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_likes'),
        ('accounts', '0003_alter_profile_neighborhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='posts',
            field=models.ManyToManyField(blank=True, to='posts.Post'),
        ),
    ]
