# Generated by Django 4.1.2 on 2023-07-05 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_cat',
            field=models.ForeignKey(db_column='idCatProd', default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.categoriaprod'),
        ),
    ]
