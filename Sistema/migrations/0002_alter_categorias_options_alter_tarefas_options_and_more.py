# Generated by Django 4.2.5 on 2023-12-04 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorias',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='tarefas',
            options={'verbose_name_plural': 'Tarefas'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name_plural': 'Usuarios'},
        ),
    ]