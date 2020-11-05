from django.shortcuts import render
from . import models
from packages.models import Package,PackageStudent
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import get_object_or_404

# Create your views here.


def TestView(request,package_id):
    if request.method == 'POST':
        marks = 0
        test = models.Test.objects.filter(package_id=package_id)
        for i in range(0,len(test)):
            test_id = test[i].id - 1
            if request.POST.get(str(test_id+1)) == test[i].correct:
                marks = marks + test[i].marks
            else:
                continue
        
        packagestudent = get_object_or_404(PackageStudent,package=package_id,student=request.user)

        packagestudent.marks = marks
        packagestudent.submission = True
        packagestudent.save()
        return HttpResponseRedirect(reverse('tests:test_successful'))
    else:
        try:
            ps = PackageStudent.objects.get(package_id=package_id,student_id=request.user.id,package__q_visibility=True,submission=False)
            data = ps.package.package_test.all()
        except:
            return HttpResponseRedirect(reverse('tests:test_denied'))

        package_end_date = get_object_or_404(Package,id=package_id).end_time
        # package_start_date = get_object_or_404(Package,id=package_id).start_time
        return render(request,'tests/test.html',{'form':data,'end_date':str(package_end_date)})


