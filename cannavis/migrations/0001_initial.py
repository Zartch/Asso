# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('espai', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipologia', models.CharField(choices=[('cog', 'cogollo'), ('exi', 'extración ice'), ('bho', 'extración bho'), ('oil', 'extración oil'), ('cre', 'crema'), ('pol', 'pollen'), ('ros', 'rosim')], max_length=3)),
                ('grams_inicials', models.FloatField()),
                ('grams_restants', models.FloatField(null=True)),
                ('data_creacio', models.DateField(auto_now_add=True)),
                ('data_modificacio', models.DateField(null=True)),
                ('actiu', models.BooleanField(default=True)),
                ('lot_referencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cannavis.Lots')),
                ('plantacio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='espai.Plantacio')),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codi', models.CharField(max_length=10, null=True)),
                ('es_mare', models.BooleanField(default=False)),
                ('data_esqueix', models.DateField(null=True)),
                ('data_creixemet', models.DateField(null=True)),
                ('data_floracio', models.DateField(null=True)),
                ('data_recollida', models.DateField(null=True)),
                ('data_final', models.DateField(null=True)),
                ('pes', models.FloatField(null=True)),
                ('banc', models.CharField(max_length=25)),
                ('esesqueix', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cannavis.Planta')),
                ('lloc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espai.Ubicacio')),
                ('plantacio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espai.Plantacio')),
            ],
        ),
        migrations.CreateModel(
            name='Varietat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('procedencia', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='planta',
            name='varietat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cannavis.Varietat'),
        ),
        migrations.AddField(
            model_name='lots',
            name='plantes',
            field=models.ManyToManyField(blank=True, to='cannavis.Planta'),
        ),
        migrations.AddField(
            model_name='lots',
            name='ubicacio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='espai.Ubicacio'),
        ),
    ]
