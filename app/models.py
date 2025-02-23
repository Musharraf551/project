from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.Category_name