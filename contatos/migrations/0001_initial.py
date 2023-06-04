# Generated by Django 4.2.1 on 2023-06-03 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('contato', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=50)),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrdemServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aparelho', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=20)),
                ('serial', models.CharField(max_length=20)),
                ('observacao', models.TextField()),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contatos.cliente')),
            ],
        ),
    ]
