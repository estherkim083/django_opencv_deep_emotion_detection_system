# Generated by Django 4.0.3 on 2022-04-27 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_photozonedata_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='photozonedata',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 13, 31, 36, 458537, tzinfo=utc)),
        ),
    ]
