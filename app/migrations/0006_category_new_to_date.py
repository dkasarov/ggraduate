# Generated by Django 2.1.4 on 2018-12-29 11:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='new_to_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 5, 11, 56, 36, 783675, tzinfo=utc)),
        ),
    ]
