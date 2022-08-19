# Generated by Django 4.0.6 on 2022-08-17 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club_app', '0004_profesores_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividades',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='actividades',
            name='profesores',
        ),
        migrations.AlterField(
            model_name='profesores',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='profesores'),
        ),
    ]
