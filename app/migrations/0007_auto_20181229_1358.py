# Generated by Django 2.1.4 on 2018-12-29 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_category_new_to_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='new_to_date',
            field=models.DateField(default=datetime.datetime(2019, 1, 5, 11, 58, 2, 53853, tzinfo=utc)),
        ),
    ]