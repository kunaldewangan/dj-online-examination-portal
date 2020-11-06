from django.db import models
from packages.models import Package
from django.contrib import auth
# Create your models here.

class Test(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE,related_name='package_test')
    Q_no = models.IntegerField(verbose_name='Question No.')
    question = models.TextField(default="")
    option_1 = models.CharField(max_length=250)
    option_2 = models.CharField(max_length=250)
    option_3 = models.CharField(max_length=250)
    option_4 = models.CharField(max_length=250)
    correct = models.CharField(verbose_name='Correct Option',max_length=250,help_text='Please Choose one option from above option')
    marks = models.IntegerField(verbose_name='Marks on Question')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['package','timestamp']
