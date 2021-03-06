# Generated by Django 3.1.1 on 2020-11-26 13:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201027_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoughtStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('expense_price', models.FloatField()),
                ('budget_left', models.FloatField()),
                ('sold_quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.FloatField(default=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='watchlist',
        ),
        migrations.CreateModel(
            name='WatchedStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stock')),
            ],
        ),
        migrations.CreateModel(
            name='SoldStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('earning_price', models.FloatField()),
                ('budget_left', models.FloatField()),
                ('gain_price', models.FloatField()),
                ('bought_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_stock', to='myapp.boughtstock')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_stocks', to='myapp.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationAnalystRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('B', 'Buy'), ('MB', 'Moderate Buy'), ('H', 'Hold'), ('MS', 'Moderate Sell'), ('S', 'Sell')], default='B', max_length=20)),
                ('threshold_recommenders_percentage', models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('fired', models.BooleanField(default=False)),
                ('watched_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommendation_analyst_rules', to='myapp.watchedstock')),
            ],
        ),
        migrations.CreateModel(
            name='PriceThresholdRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.CharField(choices=[('B', 'Below threshold'), ('A', 'Above threshold'), ('O', 'On threshold')], default='A', max_length=20)),
                ('price_threshold', models.FloatField(default=0)),
                ('fired', models.BooleanField(default=False)),
                ('watched_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price_threshold_rules', to='myapp.watchedstock')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('is_read', models.BooleanField(default=False)),
                ('stock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='myapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeThresholdRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.CharField(choices=[('B', 'Below threshold'), ('A', 'Above threshold'), ('O', 'On threshold')], default='A', max_length=20)),
                ('percentage_threshold', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(-100)])),
                ('fired', models.BooleanField(default=False)),
                ('watched_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_threshold_rules', to='myapp.watchedstock')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeStatusRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'Negative'), ('P', 'Positive')], default='P', max_length=10)),
                ('num_of_days', models.PositiveIntegerField(default=30, validators=[django.core.validators.MaxValueValidator(360), django.core.validators.MinValueValidator(2)])),
                ('fired', models.BooleanField(default=False)),
                ('watched_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_status_rules', to='myapp.watchedstock')),
            ],
        ),
        migrations.AddField(
            model_name='boughtstock',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bought_stocks', to='myapp.portfolio'),
        ),
        migrations.AddField(
            model_name='boughtstock',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.stock'),
        ),
        migrations.AddField(
            model_name='profile',
            name='portfolio',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='myapp.portfolio'),
        ),
    ]
