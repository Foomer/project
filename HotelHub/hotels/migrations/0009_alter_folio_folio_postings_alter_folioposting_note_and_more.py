# Generated by Django 5.0.1 on 2024-01-13 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_rename_enddate_event_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folio',
            name='folio_postings',
            field=models.ManyToManyField(blank=True, related_name='folio_postings', to='hotels.folioposting'),
        ),
        migrations.AlterField(
            model_name='folioposting',
            name='note',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('amount', models.FloatField()),
                ('note', models.TextField(blank=True)),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='hotels.folio')),
            ],
        ),
        migrations.AddField(
            model_name='folio',
            name='payment',
            field=models.ManyToManyField(blank=True, related_name='folios', to='hotels.payment'),
        ),
    ]
