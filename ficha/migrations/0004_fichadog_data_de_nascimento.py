# Generated by Django 4.2 on 2023-05-20 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ficha', '0003_remove_fichadog_data_de_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichadog',
            name='data_de_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]