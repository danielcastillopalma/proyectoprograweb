# Generated by Django 4.1.2 on 2023-07-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_producto_img_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img_prod',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
