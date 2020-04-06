from django.db import models

# Create your models here.

class Dept(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=128)

class Emp(models.Model):
    # 员工表
    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=64, db_index=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    sex = models.CharField(max_length=16, choices=gender, default='男')
    dept = models.ForeignKey(Dept, db_index=True, db_column='dept_id', on_delete=models.CASCADE)
    leader = models.ForeignKey('self', db_index=True, db_column='leader_id', null=True, blank=True, on_delete=models.CASCADE)

class Attendance(models.Model):
    # 考勤表
    emp = models.ForeignKey(Emp, db_index=True, db_column='emp_id', on_delete=models.CASCADE)
    date = models.CharField(max_length=10, db_index=True)
    on_work_time = models.CharField(max_length=20, null=True)
    off_work_time = models.CharField(max_length=20, null=True)

