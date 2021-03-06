# Generated by Django 2.2.13 on 2020-08-03 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200803_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='etime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 3, 19, 26, 33, 261611), null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='stime',
            field=models.TimeField(default=datetime.datetime(2020, 8, 3, 19, 26, 33, 261611), null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='category',
            field=models.CharField(choices=[('F', 'Food'), ('A', 'Auditorium'), ('S', 'Sports'), ('D', 'Department')], max_length=50, null=True),
        ),
    ]
