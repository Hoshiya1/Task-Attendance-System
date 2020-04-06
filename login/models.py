from django.db import models
from base.models import Emp

# Create your models here.
class User(models.Model):
    id = models.OneToOneField(Emp, primary_key=True, on_delete=models.CASCADE, db_column='id')
    password = models.CharField(max_length=256)