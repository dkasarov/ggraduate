# Generated by Django 2.1.4 on 2019-01-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20190105_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapi',
            name='name_url',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
