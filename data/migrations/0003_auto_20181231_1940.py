# Generated by Django 2.1.4 on 2018-12-31 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20181231_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapi',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
