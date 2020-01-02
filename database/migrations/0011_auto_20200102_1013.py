# Generated by Django 3.0 on 2020-01-02 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20191227_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fk_id_admin',
        ),
        migrations.RemoveField(
            model_name='pacjent',
            name='dokumenty',
        ),
        migrations.RemoveField(
            model_name='wizyta',
            name='dokumenty',
        ),
        migrations.AddField(
            model_name='dokument',
            name='wizyta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.Wizyta'),
        ),
    ]
