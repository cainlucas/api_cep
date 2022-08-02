# Generated by Django 4.0.6 on 2022-07-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meucep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('cidade', models.CharField(max_length=36)),
                ('bairro', models.CharField(max_length=36)),
                ('rua', models.CharField(max_length=120)),
                ('complemento', models.CharField(max_length=200)),
            ],
        ),
    ]
