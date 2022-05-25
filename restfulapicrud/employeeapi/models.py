from django.db import models

class Employee(models.Model):

    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)

    # Create / Insert

    