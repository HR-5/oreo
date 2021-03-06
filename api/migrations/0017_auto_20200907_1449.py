# Generated by Django 2.2.13 on 2020-09-07 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200907_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='etime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 7, 14, 49, 24, 679353), null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='stime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 7, 14, 49, 24, 679353), null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(choices=[('S', 'Sports'), ('D', 'Department'), ('A', 'Auditorium'), ('F', 'Food')], max_length=50, null=True),
        ),
    ]
