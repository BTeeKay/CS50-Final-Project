# Generated by Django 3.2.8 on 2021-11-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('Name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('Metal', models.PositiveIntegerField(default=1000)),
                ('Hydrogen', models.PositiveIntegerField(default=1000)),
                ('AntiMatter', models.PositiveIntegerField(default=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
