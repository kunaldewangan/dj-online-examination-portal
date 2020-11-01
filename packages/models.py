from django.db import models
from django.contrib import auth
# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    visibility = models.BooleanField(default=False)
    no_of_Q = models.IntegerField()
    total_marks = models.IntegerField()
    participants = models.ManyToManyField(auth.get_user_model(),through='PackageStudent')
    duration = models.DurationField()
    date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['timestamp']

class PackageStudent(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE,related_name='package_student')
    student = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE,related_name='student_package')
    marks = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{user}({package})".format(user=self.student.username,package=self.package.name)

    class Meta:
        unique_together = ('package','student')



