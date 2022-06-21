# Generated by Django 3.2 on 2022-06-08 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0001_initial'),
        ('accounts', '0002_alter_profile_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborhoods.neighborhood'),
        ),
    ]
