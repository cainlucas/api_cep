# Generated by Django 4.0.6 on 2022-07-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_meucep_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meucep',
            name='bairro',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='meucep',
            name='cidade',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='meucep',
            name='rua',
            field=models.CharField(max_length=512),
        ),
    ]
