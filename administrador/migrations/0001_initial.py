# Generated by Django 4.1.2 on 2023-06-17 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.AutoField(db_column='idTipo', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
                ('stock', models.CharField(max_length=100)),
                ('id_tipo', models.ForeignKey(db_column='idTipo', on_delete=django.db.models.deletion.CASCADE, to='administrador.tipo')),
            ],
        ),
    ]
