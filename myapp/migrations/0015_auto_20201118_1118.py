# Generated by Django 3.1.1 on 2020-11-18 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_delete_activityperiodrule'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendationanalystrule',
            name='category',
            field=models.CharField(choices=[('B', 'Buy'), ('MB', 'Moderate Buy'), ('H', 'Hold'), ('MS', 'Moderate Sell'), ('S', 'Sell')], default='B', max_length=20),
        ),
        migrations.AddField(
            model_name='recommendationanalystrule',
            name='fired',
            field=models.BooleanField(default=False),
        ),
    ]