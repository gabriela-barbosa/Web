# Generated by Django 2.2.6 on 2019-12-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuSite', '0016_auto_20191213_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Preco'),
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
    ]
