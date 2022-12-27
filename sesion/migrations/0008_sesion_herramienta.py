# Generated by Django 2.1.5 on 2020-07-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0007_tablero'),
    ]

    operations = [
        migrations.AddField(
            model_name='sesion',
            name='Herramienta',
            field=models.CharField(choices=[('Peluche MoFi', 'Peluche MoFi'), ('Juegos Serios', 'Juegos Serios'), ('Tablero Mofi', 'Tablero Mofi'), ('Tablero MoPe', 'Tablero MoPe'), ('Varita', 'Varita')], default='Peluche MoFi', max_length=20, verbose_name='Herramienta usada'),
        ),
    ]
