# Generated by Django 2.1.5 on 2020-01-24 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0004_auto_20200124_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peluche',
            name='Ayuda',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=2, verbose_name='Necesita Ayuda'),
        ),
    ]