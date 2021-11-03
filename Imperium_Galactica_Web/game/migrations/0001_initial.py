# Generated by Django 3.2.8 on 2021-11-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('Name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('Metal', models.PositiveIntegerField(default=1000)),
                ('Hydrogen', models.PositiveIntegerField(default=1000)),
                ('AntiMatter', models.PositiveIntegerField(default=1000)),
            ],
        ),
    ]
