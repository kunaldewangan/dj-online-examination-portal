from django.db import models
from django.contrib import auth
# Create your models here.

class Package(models.Model):
    name = models.CharField(verbose_name='Package Name',max_length=250)
    description = models.TextField()
    visibility = models.BooleanField(verbose_name='Package visible?',default=False)
    no_of_Q = models.IntegerField(verbose_name='Total No. Of Questions')
    q_visibility = models.BooleanField(verbose_name='Question visible?',default=False,help_text='click if you want to show Questions')
    total_marks = models.IntegerField()
    participants = models.ManyToManyField(auth.get_user_model(),through='PackageStudent')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField(verbose_name='Test Duration',help_text='Format HH:MM:SS')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['start_time']

class PackageStudent(models.Model):
    package = models.ForeignKey(Package,on_delete=models.CASCADE,related_name='package_student')
    student = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE,related_name='student_package')
    marks = models.IntegerField(default=0,help_text='It is automatic field. please dont select it.')
    submission = models.BooleanField(verbose_name='Submission',default=False,help_text='It is automatic field. please dont select it.')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{user}({package})".format(user=self.student.username,package=self.package.name)

    class Meta:
        unique_together = ('package','student')



