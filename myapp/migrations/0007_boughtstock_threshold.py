# Generated by Django 3.1.1 on 2020-11-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20201126_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='boughtstock',
            name='threshold',
            field=models.FloatField(null=True),
        ),
    ]
