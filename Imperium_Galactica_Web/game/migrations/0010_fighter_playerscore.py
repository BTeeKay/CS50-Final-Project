# Generated by Django 3.2.8 on 2021-11-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_hcollector_particlecollider_shipfactory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Steel', models.PositiveIntegerField(default=1000)),
                ('Hydrogen', models.PositiveIntegerField(default=1000)),
                ('AntiMatter', models.PositiveIntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('Name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('Score', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]