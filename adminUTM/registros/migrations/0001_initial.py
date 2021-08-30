# Generated by Django 3.2.4 on 2021-08-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrarEmpleados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Usuario')),
                ('nombre', models.TextField()),
                ('apellidoPa', models.TextField()),
                ('apellidoMa', models.TextField()),
                ('area', models.TextField()),
                ('turno', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='fotos', verbose_name='Imagen del usuario')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Administrar empleado',
                'verbose_name_plural': 'Administrar empleados',
                'ordering': ['-created'],
            },
        ),
    ]