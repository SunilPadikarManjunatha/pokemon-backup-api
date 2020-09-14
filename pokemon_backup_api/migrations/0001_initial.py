# Generated by Django 2.1 on 2020-09-13 00:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('backup_on', models.DateTimeField(auto_now=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
