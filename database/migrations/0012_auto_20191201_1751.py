# Generated by Django 2.2.7 on 2019-12-01 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20191201_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='fk_id_Lekarz',
            new_name='fk_id_lekarz',
        ),
    ]