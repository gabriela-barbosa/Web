# Generated by Django 2.2.6 on 2019-10-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuSite', '0004_servico_frasedestaque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='fraseDestaque',
            field=models.CharField(blank=True, max_length=200, verbose_name='Frase'),
        ),
    ]