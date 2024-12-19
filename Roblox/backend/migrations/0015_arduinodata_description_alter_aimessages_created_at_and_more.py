# Generated by Django 5.1 on 2024-09-09 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_aimessages_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arduinodata',
            name='description',
            field=models.CharField(default='provide More information about why farmer should plant the crop you specified', max_length=300),
        ),
        migrations.AlterField(
            model_name='aimessages',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 15, 3, 18, 815404, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='arduinodata',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 15, 3, 18, 822133, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='cropspecs',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 15, 3, 18, 820134, tzinfo=datetime.timezone.utc)),
        ),
    ]
