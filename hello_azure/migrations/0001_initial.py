# Generated by Django 4.2.2 on 2024-06-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MisCursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=15)),
                ('cursos', models.CharField(max_length=255, null=True)),
                ('certificado', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MisDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('correo', models.CharField(max_length=60, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('empresa', models.CharField(max_length=255, null=True)),
                ('codigo', models.CharField(max_length=15, null=True)),
                ('usuario', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=2, null=True)),
                ('joined_date', models.DateField(null=True)),
            ],
        ),
    ]