# Generated by Django 3.0.5 on 2020-05-02 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apparchar', '0003_eventocalificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apparchar.Evento'),
        ),
        migrations.AlterField(
            model_name='calificacion',
            name='usuariocliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apparchar.cliente'),
        ),
        migrations.DeleteModel(
            name='EventoCalificacion',
        ),
    ]
