# Generated by Django 3.2 on 2021-05-04 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IntApp', '0003_asignatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='asignatura',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='IntApp.asignatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='nombre',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
