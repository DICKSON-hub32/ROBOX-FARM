# Generated by Django 5.1 on 2024-09-19 07:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_climatelocation_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropspecs',
            name='Altitude',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cropspecs',
            name='No_of_irigation_per_day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cropspecs',
            name='No_of_irigation_per_week',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cropspecs',
            name='Soil_pH',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='aimessages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 7, 6, 20, 453923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='arduinodata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 7, 6, 20, 455924, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='climateaveragedatapermonth',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 7, 6, 20, 456923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='climatelocation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 7, 6, 20, 456923, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cropspecs',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 7, 6, 20, 454924, tzinfo=datetime.timezone.utc)),
        ),
    ]
