# Generated by Django 5.0.1 on 2024-01-09 15:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_rename_createddate_roomservice_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='eventType',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='roomservice',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='EventAttendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfDependees', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.event')),
                ('guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.guest')),
            ],
        ),
    ]
