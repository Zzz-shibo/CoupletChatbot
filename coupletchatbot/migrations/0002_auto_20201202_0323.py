# Generated by Django 3.1.2 on 2020-12-02 03:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coupletchatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpus',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]