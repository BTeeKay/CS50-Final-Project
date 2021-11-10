from django.db import models
from django.contrib.auth.models import User


class Commodity(models.Model):

    Name = models.CharField(primary_key = True, unique=True, max_length=64)
    Metal = models.PositiveIntegerField(default=1000)
    Hydrogen = models.PositiveIntegerField(default=1000) 
    AntiMatter = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"{self.Name}"


class Building(models.Model):

    Name = models.CharField(primary_key = True, unique=True, max_length=64)
    SteelMill = models.PositiveIntegerField(default=0)
    HCollector = models.PositiveIntegerField(default=0)
    ParticleCollider = models.PositiveIntegerField(default=0)
    ShipFactory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.Name}"


class Fleet(models.Model):

    Name = models.CharField(primary_key = True, unique=True, max_length=64)
    Fighter = models.PositiveIntegerField(default=0)
    HeavyFighter = models.PositiveIntegerField(default=0)
    Destroyer = models.PositiveIntegerField(default=0)
    Corvette = models.PositiveIntegerField(default=0)
    Cruiser = models.PositiveIntegerField(default=0)
    Battleship = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.Name}"

class SteelMills(models.Model):

    Level = models.AutoField(primary_key=True)
    Steel = models.PositiveIntegerField(default=0)
    Hydrogen = models.PositiveIntegerField(default=0)
    AntiMatter = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.Level}"

class HCollector(models.Model):

    Level = models.AutoField(primary_key=True)
    Steel = models.PositiveIntegerField(default=0)
    Hydrogen = models.PositiveIntegerField(default=0)
    AntiMatter = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.Level}"

class ParticleCollider(models.Model):

    Level = models.AutoField(primary_key=True)
    Steel = models.PositiveIntegerField(default=0)
    Hydrogen = models.PositiveIntegerField(default=0)
    AntiMatter = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.Level}"

class ShipFactory(models.Model):

    Level = models.AutoField(primary_key=True)
    Steel = models.PositiveIntegerField(default=0)
    Hydrogen = models.PositiveIntegerField(default=0)
    AntiMatter = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.Level}"


class PlayerScore(models.Model):

    Name = models.CharField(primary_key = True, unique=True, max_length=64)
    Score = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.Score}"