# Generated by Django 5.0.1 on 2024-01-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(default='Standart', max_length=25)),
                ('capacity', models.SmallIntegerField()),
                ('floor', models.IntegerField()),
                ('description', models.TextField()),
                ('price_per_night', models.FloatField()),
            ],
        ),
    ]
