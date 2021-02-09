# Generated by Django 3.1.6 on 2021-02-09 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_auto_20210208_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='description',
        ),
        migrations.AddField(
            model_name='games',
            name='maker',
            field=models.CharField(default='Taco', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='skill_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
