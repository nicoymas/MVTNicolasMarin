from django.db import models

class Familia (models.Model):
    id=models.AutoField(primary_key=True)
    fecha_nac=models.DateField()
    fam_list=models.CharField(max_length=40)
    edad=models.IntegerField()

