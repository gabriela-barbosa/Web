# Generated by Django 2.2.6 on 2019-10-06 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meuSite', '0005_auto_20191006_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='fraseDestaque',
        ),
        migrations.CreateModel(
            name='DestaqueServicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(blank=True)),
                ('fraseDestaque', models.CharField(blank=True, max_length=200, verbose_name='Frase')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuSite.Servico')),
            ],
            options={
                'db_table': 'destaqueServico',
            },
        ),
    ]