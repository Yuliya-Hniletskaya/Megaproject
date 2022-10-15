from django.contrib import admin

from Book_info import models
from Book_info.models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_of_birth', 'date_of_death')
    
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)
admin.site.register(models.Series)