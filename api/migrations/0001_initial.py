# Generated by Django 3.0.7 on 2020-09-16 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('salario', models.FloatField(null=True)),
                ('local', models.CharField(max_length=20)),
                ('quantidade', models.IntegerField()),
                ('contato', models.EmailField(max_length=254)),
                ('tipo_contratacao', models.CharField(max_length=3)),
                ('tecnologias', models.ManyToManyField(to='api.Tecnologia')),
            ],
        ),
    ]