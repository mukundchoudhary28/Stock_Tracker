# Generated by Django 3.2.4 on 2021-06-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210624_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_name',
            name='ticker',
            field=models.CharField(max_length=200),
        ),
    ]
