from django.db import models

# Create your models here.
class Employee_Model(models.Model):
    Name = models.CharField(max_length=100,null=True)
    Designation = models.CharField(max_length=100,null=True)

    Basic_salary = models.FloatField(null=True)

    HAR_percent = models.FloatField(null=True)
    DA_percent = models.FloatField(null=True)
    TA_percent = models.FloatField(null=True)

    Bonus = models.FloatField(default=0,null=True)
    Overtime_hours = models.IntegerField(default=0,null=True)
    gross_salary = models.IntegerField(null=True)
    Picture = models.ImageField(upload_to='Picture',null=True)
    
    def __str__(self):
        return self.Name