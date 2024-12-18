# Generated by Django 5.1 on 2024-09-09 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_arduinodata_description_alter_aimessages_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropspecs',
            name='isChosen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aimessages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 23, 52, 19, 941687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='arduinodata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 23, 52, 19, 941687, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cropspecs',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 23, 52, 19, 941687, tzinfo=datetime.timezone.utc)),
        ),
    ]
