# Generated by Django 5.0.3 on 2024-04-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_observer',
            field=models.BooleanField(default=True),
        ),
    ]
