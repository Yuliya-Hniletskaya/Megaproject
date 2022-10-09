from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Author's name"
        # blank=False,
        # null=False
    )
    date_of_birth = models.DateField(
        verbose_name="Date of birth"
    )
    date_of_death = models.DateField(
        verbose_name="Date of death",
        blank=True,
        null=True
    )
    description = models.TextField(
         blank=True,
         null=True
    )
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.name
    
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
    def __str__(self):
        return self.name
        
        
        
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
    def __str__(self):
        return self.name