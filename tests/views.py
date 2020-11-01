from django.shortcuts import render
from . import models
from packages.models import Package,PackageStudent
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.


def TestView(request,package_id):
    if request.method == 'POST':
        marks = 0
        test = models.Test.objects.filter(package_id=package_id)
        for i in range(0,len(test)):
            # print(i)
            test_id = test[i].id - 1
            # print('you selected option:',request.POST.get(str(test_id+1)))
            # print('answer is:',test[i].correct)
            # print('marks on Q:',test[i].marks)
            # print('test id from db:',test[i].id)
            # print('test id from form is:',request.POST.get(str(test_id+1)))
            if request.POST.get(str(test_id+1)) == test[i].correct:
                marks = marks + test[i].marks
            else:
                continue
        
        packagestudent = get_object_or_404(PackageStudent,package=package_id,student=request.user)
        
        # packagestudent = PackageStudent.objects.filter(student=request.user,package=package_id)
        packagestudent.marks = marks
        packagestudent.save()
        # print('your packge:',packagestudent.package.name)
        # print('your marks is:',marks)

        # print(request.POST.get('o2'))
        return HttpResponseRedirect(reverse('tests:test_successful'))
    else:
        data = models.Test.objects.filter(package_id=package_id)
        package_date = get_object_or_404(Package,id=package_id).date
        # print('package date is:',str(package_date))
        # print('package id is:',package_id)
        return render(request,'tests/test.html',{'form':data,'package_date':str(package_date)})


