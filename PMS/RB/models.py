from django.db import models
class Employee(models.Model):  
    Code = models.CharField(max_length=20,primary_key=True)  
    Name = models.CharField(max_length=100)  
    Email = models.EmailField()  
    Shift = models.CharField(max_length=15)  
    Dept =  models.CharField(max_length=20)  
    class Meta:  
        db_table = "employee"  
class Login(models.Model):
    Firstname=models.CharField(max_length=20)  
    Lastname=models.CharField(max_length=20)  
    Username=models.CharField(max_length=20,primary_key=True)  
    Password=models.CharField(max_length=100)
    Email= models.EmailField()
    Dob=models.DateField()  
    class Meta:
        db_table = "login_cred"

