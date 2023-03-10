# Generated by Django 4.1.6 on 2023-02-09 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPadministracion', '0003_alter_torneo_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=140),
        ),
    ]
