# Generated by Django 3.2 on 2022-06-20 08:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighborhoods', '0004_auto_20220609_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='occupants',
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='occupants',
            field=models.ManyToManyField(related_name='occupants', to=settings.AUTH_USER_MODEL),
        ),
    ]