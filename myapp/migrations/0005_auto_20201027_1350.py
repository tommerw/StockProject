# Generated by Django 3.1.1 on 2020-10-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='change_percent',
            field=models.FloatField(null=True),
        ),
    ]
