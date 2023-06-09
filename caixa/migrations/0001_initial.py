# Generated by Django 4.2.2 on 2023-06-13 05:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaixaDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('relatorio_estadia', models.TextField(max_length=500)),
                ('desconto', models.DecimalField(decimal_places=1, max_digits=3)),
                ('metodo_de_pagamento', models.CharField(choices=[('Cartão de Crédito', 'Cartão de Crédito'), ('Cartão de Debito', 'Cartão de Debito'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField(default=datetime.date.today)),
                ('num_reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.reservaday')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.fichadog')),
            ],
            options={
                'db_table': 'CaixaDay',
            },
        ),
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('relatorio_estadia', models.TextField(max_length=500)),
                ('desconto', models.DecimalField(decimal_places=1, max_digits=3)),
                ('metodo_de_pagamento', models.CharField(choices=[('Cartão de Crédito', 'Cartão de Crédito'), ('Cartão de Debito', 'Cartão de Debito'), ('Dinheiro', 'Dinheiro'), ('Pix', 'Pix')], max_length=20)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField(default=datetime.date.today)),
                ('num_reserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.reserva')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.fichadog')),
            ],
            options={
                'db_table': 'Caixa',
            },
        ),
    ]
