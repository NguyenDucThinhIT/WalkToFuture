# Generated by Django 4.0.3 on 2022-05-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='checkout_date',
            field=models.DateTimeField(),
        ),
    ]
