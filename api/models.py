from django.db import models

# Create your models here.
'''员工表'''
class BaseEmp(models.Model):
    is_work=models.BooleanField(default=True)
    entry_time=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    class Meta:
        abstract=True

class Employee(BaseEmp):
    gender_choice=(
        (0,'male'),
        (1,'female'),
        (2,'other')
    )
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    gender = models.SmallIntegerField(choices=gender_choice, default=0)
    tell=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='pic',default='pic/1.jpg')
    class Meta:
        db_table='zhf_emp'
        verbose_name='狗蛋的员工'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

