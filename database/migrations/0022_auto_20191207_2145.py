# Generated by Django 3.0 on 2019-12-07 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_auto_20191207_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pacjent',
            options={'ordering': ('id',)},
        ),
    ]
