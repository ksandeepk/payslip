from django.db import models


# Create your models here.
class esal(models.Model):
    E_id=models.CharField(max_length=10)
    designation=models.CharField(max_length=50)
    Basic=models.FloatField()
    PF=models.FloatField(max_length=15)
    DA=models.FloatField()
    TA=models.FloatField()
    HRA=models.FloatField()
    Special_allowance=models.FloatField()
    PF=models.FloatField()
    Pension=models.FloatField()
    Insurence=models.FloatField()
    ESI=models.FloatField()
    Gross_Sal=models.FloatField()
    Net_Sal=models.FloatField()
    leaves_taken=models.FloatField()
    total_workingdays=models.FloatField()
    lop=models.FloatField()

class edeta(models.Model):
    E_name=models.CharField(max_length=25)
    designation=models.CharField(max_length=25)
    Basic=models.FloatField()
 