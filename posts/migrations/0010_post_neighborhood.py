# Generated by Django 3.2 on 2022-06-16 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0004_auto_20220609_2318'),
        ('posts', '0009_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neighborhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='neighborhoods.neighborhood'),
            preserve_default=False,
        ),
    ]