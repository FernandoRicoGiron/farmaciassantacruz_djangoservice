# Generated by Django 2.1.1 on 2018-11-23 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181023_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Direccion', models.TextField()),
                ('Imagen', models.ImageField(upload_to='Previo')),
                ('Horario', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=100)),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='Estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Estado'),
        ),
    ]
