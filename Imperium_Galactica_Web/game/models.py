from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Resource(models.Model):
#     # Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="USERNAME")
#     Name = models.CharField(primary_key = True, unique=True, max_length=64)
#     Metal = models.PositiveIntegerField(default=1000)
#     Hydrogen = models.PositiveIntegerField(default=1000) 
#     AntiMatter = models.PositiveIntegerField(default=1000)

#     def __str__(self):
#         return f"{self.Name} has {self.Metal}, {self.Hydrogen}, {self.AntiMatter}"

class Commodity(models.Model):

    Name = models.CharField(primary_key = True, unique=True, max_length=64)
    Metal = models.PositiveIntegerField(default=1000)
    Hydrogen = models.PositiveIntegerField(default=1000) 
    AntiMatter = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"{self.Name}"