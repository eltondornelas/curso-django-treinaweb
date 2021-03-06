# Generated by Django 2.1.3 on 2020-06-22 22:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=50)),
                ('sex', models.CharField(
                    choices=[('F', 'Feminino'), ('M', 'Masculino'),
                             ('N', 'Nenhuma das opções')], max_length=1)),
            ],
        ),
    ]
