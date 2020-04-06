from django.db import models
from base.models import Emp
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Task(models.Model):

    gender = (
        ('1', '仅本部门可见'),
        ('2', '公开'),
    )
    emp = models.ForeignKey(Emp, db_index=True, db_column='emp_id', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    secret_lv = models.CharField(max_length=1, choices=gender)
    completed = models.BooleanField(default=False)
    feel = models.TextField(null=True)

class TaskDetail(models.Model):
    id = models.OneToOneField(Task, on_delete=models.CASCADE, db_column='id', primary_key=True)
    detail = models.TextField(null=True)