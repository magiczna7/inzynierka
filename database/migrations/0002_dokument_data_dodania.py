# Generated by Django 3.0 on 2019-12-08 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dokument',
            name='data_dodania',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
