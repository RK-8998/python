from django.db import models

class emp_tbl(models.Model):
    userName = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    empCode = models.TextField()
    dept = models.TextField()
    designation = models.TextField()
    grade = models.TextField()
    isApproved = models.IntegerField()
    password = models.TextField(default='password')

