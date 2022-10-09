from django.db import models

# Create your models here.

class Publisher_series(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Series"
    ) 
    amount_of_books_in_series = models.IntegerField()
    description = models.TextField(
         blank=True,
         null=True
    )