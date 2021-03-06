# Generated by Django 3.0.6 on 2020-05-30 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_conta', models.CharField(choices=[('RB', 'A receber'), ('PG', 'A pagar')], max_length=2, verbose_name='Tipo de Conta')),
                ('vencimento', models.DateField(verbose_name='vencimento')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='valor R$')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.Pessoa', verbose_name='Pessoa')),
            ],
        ),
    ]
