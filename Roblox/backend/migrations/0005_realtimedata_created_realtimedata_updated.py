# Generated by Django 5.1 on 2024-08-20 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_realtimedata_humidity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtimedata',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 20, 7, 40, 6, 23463, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='realtimedata',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
