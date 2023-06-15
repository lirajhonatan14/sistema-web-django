# Generated by Django 4.2.1 on 2023-06-01 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ficha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantidade_dias', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('num_reserva', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('horario_alimentacao', models.CharField(choices=[('2x_dia', 'Duas vezes por dia'), ('3x_dia', 'Três vezes por dia'), ('personalizado', 'Horário personalizado')], max_length=20)),
                ('horario_personalizado', models.CharField(blank=True, max_length=20, null=True)),
                ('instrucoes_medicamentos', models.CharField(blank=True, max_length=100, null=True)),
                ('autorizacao_para_cuidados_medicos', models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False)),
                ('pago', models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False, null=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.fichadog')),
            ],
            options={
                'db_table': 'Reserva_Hotel',
            },
        ),
        migrations.CreateModel(
            name='ServicosAdicionais',
            fields=[
                ('nome_servico', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('valor_servico', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'db_table': 'Servicos_adicionais',
            },
        ),
        migrations.CreateModel(
            name='ReservaServicoAdicional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(default=1)),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.reserva')),
                ('servico_adicional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.servicosadicionais')),
            ],
            options={
                'db_table': 'Reserva_Servicos_adicionais',
            },
        ),
        migrations.CreateModel(
            name='ReservaDay',
            fields=[
                ('num_reserva', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('horario_alimentacao', models.CharField(choices=[('2x_dia', 'Duas vezes por dia'), ('3x_dia', 'Três vezes por dia'), ('personalizado', 'Horário personalizado')], max_length=20)),
                ('horario_personalizado', models.CharField(blank=True, max_length=20, null=True)),
                ('instrucoes_medicamentos', models.CharField(blank=True, max_length=100, null=True)),
                ('autorizacao_para_cuidados_medicos', models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False)),
                ('pago', models.BooleanField(choices=[(False, 'Não'), (True, 'Sim')], default=False, null=True)),
                ('pacote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.pacote')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ficha.fichadog')),
                ('servicos_adicionais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.servicosadicionais')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Reserva_Day',
            },
        ),
        migrations.AddField(
            model_name='reserva',
            name='servicos_adicionais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.servicosadicionais'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
