# Generated by Django 2.1.4 on 2018-12-31 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_userapi_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='description',
            field=models.TextField(null=True),
        ),
    ]