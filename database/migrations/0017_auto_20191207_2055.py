# Generated by Django 3.0 on 2019-12-07 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20191207_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wizyta',
            name='badania',
            field=models.ManyToManyField(to='database.Badanie'),
        ),
        migrations.AlterField(
            model_name='wizyta',
            name='dokumenty',
            field=models.ManyToManyField(to='database.Dokument'),
        ),
        migrations.AlterField(
            model_name='wizyta',
            name='objawy',
            field=models.ManyToManyField(to='database.Objawy'),
        ),
    ]
