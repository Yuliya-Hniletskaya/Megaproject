from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Author's name"
    )
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    description = models.TextField(
         blank=True,
         null=True
    )
        
    