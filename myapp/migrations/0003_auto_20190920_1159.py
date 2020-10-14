# Generated by Django 2.2.4 on 2019-09-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190920_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='change',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='market_cap',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='primary_exchange',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='top_rank',
            field=models.IntegerField(null=True),
        ),
    ]
