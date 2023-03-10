# Generated by Django 2.1.5 on 2020-06-22 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estudiante', '0003_auto_20200621_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoJuegosS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FrecuenciaS', models.PositiveIntegerField(verbose_name='Frecuencia Semanal')),
                ('Topos', models.PositiveIntegerField(verbose_name='Topos')),
                ('Laberinto', models.PositiveIntegerField(verbose_name='Laberinto')),
                ('RompeC', models.PositiveIntegerField(verbose_name='RompeC')),
                ('Colorear', models.PositiveIntegerField(verbose_name='Colorear')),
                ('Letras', models.PositiveIntegerField(verbose_name='Letras')),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Estudiante', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Recomendacion Juegos Serios',
                'verbose_name_plural': 'Recomendaciones Juegos Serios',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RecoPeluche',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FrecuenciaS', models.PositiveIntegerField(verbose_name='Frecuencia Semanal')),
                ('Sombrero', models.PositiveIntegerField(verbose_name='Sombrero')),
                ('Broches', models.PositiveIntegerField(verbose_name='Broches')),
                ('Cierre', models.PositiveIntegerField(verbose_name='Cierre')),
                ('Velcro', models.PositiveIntegerField(verbose_name='Velcro')),
                ('Cordon', models.PositiveIntegerField(verbose_name='Cordon')),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Estudiante', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Recomendacion Peluche',
                'verbose_name_plural': 'Recomendaciones Peluche',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RecoTablero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FrecuenciaS', models.PositiveIntegerField(verbose_name='Frecuencia Semanal')),
                ('Trazos', models.PositiveIntegerField(verbose_name='Trazos')),
                ('Pinzas', models.PositiveIntegerField(verbose_name='Pinzas')),
                ('Precision', models.PositiveIntegerField(verbose_name='Precision')),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Estudiante', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Recomendacion Tablero',
                'verbose_name_plural': 'Recomendaciones Tablero',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RecoVarita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FrecuenciaS', models.PositiveIntegerField(verbose_name='Frecuencia Semanal')),
                ('Horizontal', models.PositiveIntegerField(verbose_name='Horizontal')),
                ('Vertical', models.PositiveIntegerField(verbose_name='Vertical')),
                ('Oblicuas', models.PositiveIntegerField(verbose_name='Oblicuas')),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiante.Estudiante', verbose_name='Estudiante')),
            ],
            options={
                'verbose_name': 'Recomendacion Varita',
                'verbose_name_plural': 'Recomendaciones Varita',
                'ordering': ['-id'],
            },
        ),
    ]
