from django.db import models

# Create your models here.

class user_attendance(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=50)
    attend_date = models.DateTimeField('date published')
    attend_status = models.CharField(max_length=1)
    emp_overtime = models.TimeField(default=0)


class user_auth(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    emp_id = models.CharField(max_length=10)
    user_title = models.CharField(max_length=30)
    created_at = models.DateField()

class emp_data(models.Model):
    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=50)
    emp_dob = models.DateField('date published')
    emp_gender = models.CharField(max_length=8)
    emp_fname = models.CharField(max_length=50)
    emp_addr = models.CharField(max_length=50)
    emp_position = models.CharField(max_length=50)
    emp_email = models.EmailField()
    emp_mnumber = models.IntegerField()
    emp_salary = models.IntegerField()
    dept_code = models.CharField(max_length=30)

class user_roles(models.Model):
    emp_id = models.CharField(max_length=10)
    user_role = models.CharField(max_length=5)


