# Generated by Django 3.0 on 2019-12-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20191227_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='daneepidemiologiczne',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
