# Generated by Django 4.2.1 on 2023-06-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_alter_cliente_contato_alter_cliente_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='contato',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
