from django.db import models

class EMPLOYEE_TBL(models.Model):
    userName = models.CharField(max_length=50), 
    firstName = models.CharField(max_length=50),
    lastName = models.CharField(max_length=50),
    email = models.CharField(max_length=50),
    empCode = models.CharField(max_length=50),
    dept = models.CharField(max_length=50),
    designation = models.CharField(max_length=50),
    grade = models.CharField(max_length=50),
    isApproved = models.IntegerField()
    
