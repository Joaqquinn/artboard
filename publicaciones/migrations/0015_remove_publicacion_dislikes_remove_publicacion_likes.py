# Generated by Django 4.2.1 on 2023-06-20 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0014_publicacion_dislikes_publicacion_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='likes',
        ),
    ]
