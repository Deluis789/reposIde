# Generated by Django 4.2 on 2024-07-31 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalleAv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True)),
                ('numero_vivienda', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ZonaUrb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.TextField()),
                ('ciudad', models.CharField(default='El alto', max_length=50)),
                ('cordenadas', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudVecino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='AAA', max_length=10)),
                ('ubicacion_direccion', models.CharField(max_length=100)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('celular', models.IntegerField()),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.distrito')),
                ('zona_urbanizacion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.zonaurb')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(default='AAA')),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('distrito', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.distrito')),
                ('zonaurb', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.zonaurb')),
            ],
        ),
    ]
