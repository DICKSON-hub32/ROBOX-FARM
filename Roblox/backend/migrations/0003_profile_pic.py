# Generated by Django 5.1 on 2024-08-19 11:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_realtimedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile_pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]