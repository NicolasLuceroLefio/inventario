# Generated by Django 5.0.6 on 2024-11-19 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
    ]
