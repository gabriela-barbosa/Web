# Generated by Django 2.2.6 on 2019-10-06 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Tipo')),
            ],
            options={
                'db_table': 'tipoServico',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=200, verbose_name='servico')),
                ('imagem', models.CharField(max_length=200, verbose_name='imagem')),
                ('descricao', models.TextField(blank=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuSite.TipoServico')),
            ],
            options={
                'db_table': 'servico',
            },
        ),
    ]
