# Generated by Django 4.0.3 on 2022-05-05 09:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_photozonedata_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photozonedata',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 9, 22, 47, 813685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shareemotion',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 9, 22, 47, 813685, tzinfo=utc)),
        ),
    ]
