# Generated by Django 5.1.2 on 2024-10-14 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steamfake', '0007_turma_curso'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aluno',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='turma',
            name='curso',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Turma',
        ),
    ]
