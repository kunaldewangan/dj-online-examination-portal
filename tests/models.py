from django.db import models
from packages.models import Package
from django.contrib import auth
# Create your models here.

class Test(models.Model):
    Q_no = models.IntegerField()
    question = models.TextField(default="")
    option_1 = models.CharField(max_length=250)
    option_2 = models.CharField(max_length=250)
    option_3 = models.CharField(max_length=250)
    option_4 = models.CharField(max_length=250)
    correct = models.CharField(max_length=250)
    marks = models.IntegerField()
    package = models.ForeignKey(Package,on_delete=models.CASCADE,related_name='package_test')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


