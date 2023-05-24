# Generated by Django 4.2.1 on 2023-05-24 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo Rol')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo Usuario')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.rol', verbose_name='Rol')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('idPublicacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo Publicacion')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('fechaPublicacion', models.DateField()),
                ('estatus', models.CharField(max_length=50)),
                ('idusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.usuario', verbose_name='Id usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('idImagen', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo Imagen')),
                ('nombre', models.TextField(max_length=20)),
                ('archivo', models.CharField(max_length=20)),
                ('idPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion', verbose_name='Id publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('idComentario', models.AutoField(primary_key=True, serialize=False, verbose_name='Codigo Comentario')),
                ('comentario', models.TextField(max_length=500)),
                ('fechaComentario', models.DateField(verbose_name='')),
                ('estatus', models.CharField(max_length=50)),
                ('idPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion', verbose_name='Id publicacion')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.usuario', verbose_name='Id usuario')),
            ],
        ),
    ]