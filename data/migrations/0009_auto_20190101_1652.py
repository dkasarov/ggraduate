# Generated by Django 2.1.4 on 2019-01-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_delete_typedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userapidata',
            name='typedata',
            field=models.CharField(max_length=5),
        ),
    ]
