from django.db import models

# Create your models here.

class ActiveEmps(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='Y')


class EmpModel(models.Model):
    name = models.CharField('emp_name',max_length=100)
    age = models.IntegerField('emp_age')
    salary = models.FloatField('emp_sal')
    position = models.CharField('emp_pos', max_length=100)
    gender = models.CharField('emp_gen', max_length=100)
    active = models.CharField('emp_active', max_length=100,default='Y')
    allemps = models.Manager() # default name overriden to all
    actemps = ActiveEmps() # active emps

class Address(models.Model):
    city = models.CharField('adr_city', max_length=100)
    state = models.CharField('adr_state', max_length=100)
    pincode = models.CharField('adr_pin', max_length=100)
    emp = models.ForeignKey(EmpModel,on_delete=models.CASCADE,related_name='addrs')


