# Generated by Django 4.2 on 2023-05-20 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0002_rename_veterinario_cao_fichadog_veterinario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fichadog',
            name='data_de_nascimento',
        ),
    ]
