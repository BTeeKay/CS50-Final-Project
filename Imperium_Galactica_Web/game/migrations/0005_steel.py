# Generated by Django 3.2.8 on 2021-11-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_rename_buildings_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Steel', models.PositiveIntegerField(default=0)),
                ('Hydrogen', models.PositiveIntegerField(default=0)),
                ('AntiMatter', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]