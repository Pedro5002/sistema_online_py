# Generated by Django 4.2.5 on 2023-09-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('dataNascimento', models.DateTimeField()),
                ('endereco', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
            ],
        ),
    ]
