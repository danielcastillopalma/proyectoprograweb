# Generated by Django 4.1.2 on 2023-06-30 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]