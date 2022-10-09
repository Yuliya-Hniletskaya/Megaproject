from django.db import models

# Create your models here.

class Authors(models.Model):
    name = models.CharField(
        max_length=50
        verbose_name="Author's name"
        # blank=False,
        # null=False
    )
    date_of_birth = models.DateField(
        verbose_name="Date of birth"
    )
    date_of_death = models.DateField(
        verbose_name="Daye of death"
    )
    description = models.TextField(
         blank=True,
         null=True
    )
        
    
class Series(models.Model):
    name = models.CharField(
        max_length=50,
        # blank=False,
        # null=False
    ) 
    amount_of_books_in_series = models.IntegerField()
    description = models.TextField(
         blank=True,
         null=True
    )
    
class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        # blank=False,
        # null=False
    )
    description = models.TextField(
         blank=True,
         null=True
    )
        
class Publisher(models.Model):
    name = models.CharField(
        max_length=50,
        # blank=False,
        # null=False
    )
    description = models.TextField(
         blank=True,
         null=True
    )