# Generated by Django 5.1.2 on 2024-11-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_rename_information_currencymodel_buy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencymodel',
            name='buy',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='currencymodel',
            name='ccy',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='currencymodel',
            name='sale',
            field=models.CharField(max_length=10),
        ),
    ]
