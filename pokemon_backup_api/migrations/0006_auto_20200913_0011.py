# Generated by Django 2.1 on 2020-09-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_backup_api', '0005_auto_20200913_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupitems',
            name='evolves_from',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
