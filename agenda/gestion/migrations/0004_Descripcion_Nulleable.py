# Generated by Django 4.0.3 on 2022-04-07 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_Agrege_Columna_Descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
