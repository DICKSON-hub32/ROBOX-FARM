# Generated by Django 5.1 on 2024-08-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtimedata',
            name='Humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='Moisture',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='realtimedata',
            name='Temperature',
            field=models.IntegerField(),
        ),
    ]
