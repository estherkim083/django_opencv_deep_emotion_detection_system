# Generated by Django 4.0.3 on 2022-05-02 00:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_photozonedata_create_date_statisticsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photozonedata',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 2, 0, 45, 6, 481924, tzinfo=utc)),
        ),
    ]
