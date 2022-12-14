# Generated by Django 4.0.6 on 2022-07-28 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Club_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividades',
            options={'ordering': ('actividad', 'turno')},
        ),
        migrations.AlterModelOptions(
            name='alumnos',
            options={'ordering': ('nombre', 'edad', 'actividad', 'turno')},
        ),
        migrations.AlterModelOptions(
            name='profesores',
            options={'ordering': ('nombre', 'actividad', 'turno')},
        ),
        migrations.AddField(
            model_name='actividades',
            name='profesores',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Club_app.profesores'),
        ),
        migrations.AlterUniqueTogether(
            name='actividades',
            unique_together={('actividad', 'turno')},
        ),
    ]
