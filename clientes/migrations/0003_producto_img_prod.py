# Generated by Django 4.1.2 on 2023-07-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_producto_id_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='img_prod',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
