# Generated by Django 4.0.3 on 2022-05-05 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_shareemotion_share_emotion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shareemotion',
            name='emotion_labeled_data',
        ),
        migrations.AlterField(
            model_name='photozonedata',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 11, 22, 8, 746697, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shareemotion',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 11, 22, 8, 746697, tzinfo=utc)),
        ),
    ]
