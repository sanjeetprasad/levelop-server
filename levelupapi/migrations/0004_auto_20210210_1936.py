# Generated by Django 3.1.6 on 2021-02-10 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20210209_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='location',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='scheduler',
            new_name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default='12:00'),
            preserve_default=False,
        ),
    ]