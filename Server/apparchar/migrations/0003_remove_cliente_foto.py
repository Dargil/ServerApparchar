# Generated by Django 3.0.5 on 2020-04-09 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apparchar', '0002_auto_20200408_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
    ]
