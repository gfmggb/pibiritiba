# Generated by Django 2.2.4 on 2019-11-18 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('codigo', models.CharField(max_length=25)),
                ('carga_horaria_total', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=90)),
                ('matricula', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'professores',
            },
        ),
        migrations.CreateModel(
            name='SalaDeAula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('tipo', models.CharField(choices=[('Sala regular', 'Sala regular'), ('Laboratório', 'Laboratório'), ('Audiovisual', 'Audiovisual'), ('Auditório', 'Auditório'), ('Miniauditório', 'Miniauditório')], max_length=15)),
                ('numero', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Salas de aulas',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino')], max_length=15)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'turmas',
            },
        ),
        migrations.CreateModel(
            name='SlotDeHorario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField(unique=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otime.Disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otime.Professor')),
                ('sala_de_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otime.SalaDeAula')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otime.Turma')),
            ],
            options={
                'verbose_name_plural': 'Slots de horarios',
            },
        ),
    ]
