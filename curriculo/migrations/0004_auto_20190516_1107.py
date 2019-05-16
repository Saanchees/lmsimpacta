# Generated by Django 2.1.7 on 2019-05-16 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0003_auto_20190219_0938'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatrizCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['nome']},
        ),
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='semestres',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='matrizcurricular',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curriculo.Curso'),
        ),
        migrations.AddField(
            model_name='matrizcurricular',
            name='disciplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='curriculo.Disciplina'),
        ),
        migrations.AddField(
            model_name='curso',
            name='disciplinas',
            field=models.ManyToManyField(through='curriculo.MatrizCurricular', to='curriculo.Disciplina'),
        ),
    ]
