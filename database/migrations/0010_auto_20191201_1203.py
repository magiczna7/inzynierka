# Generated by Django 2.2.7 on 2019-12-01 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20191201_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lekarz',
            name='nr_pwz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]