# Generated by Django 4.2 on 2023-06-15 18:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_cinema', '0006_remove_cinemasession_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieseason',
            name='film_duration',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
