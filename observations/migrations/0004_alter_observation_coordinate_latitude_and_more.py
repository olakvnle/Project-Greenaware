# Generated by Django 5.0.4 on 2024-04-29 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0003_observation_coordinate_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='coordinate_latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='observation',
            name='coordinate_longitute',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
