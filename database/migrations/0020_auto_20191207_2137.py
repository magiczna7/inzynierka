# Generated by Django 3.0 on 2019-12-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_auto_20191207_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jednostkachorobowa',
            name='nr_icd',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='jednostkachorobowa',
            name='opis',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='lekarz',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lekarz',
            name='surname',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='kod_pocztowy',
            field=models.CharField(blank=True, default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='miasto',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='nr_mieszkania',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='nr_ulicy',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='pesel',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='surname',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='telefon',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacjent',
            name='ulica',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='kod_pocztowy',
            field=models.CharField(blank=True, default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='miasto',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='nazwa',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='nr_mieszkania',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='nr_ulicy',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='telefon',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='przychodnia',
            name='ulica',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wizyta',
            name='uwagi',
            field=models.CharField(blank=True, default='', max_length=500),
            preserve_default=False,
        ),
    ]
