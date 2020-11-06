from django.shortcuts import render
from django.views import generic
from django.db import IntegrityError
from django.contrib import messages
from . import models
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

class PackageList(generic.ListView):
    model = models.Package

    def get_queryset(self):
        return super().get_queryset().filter(visibility=True)
    

class UserPackageList(LoginRequiredMixin,generic.ListView):
    model = models.Package
    template_name = 'packages/user_package.html'
    def get_queryset(self):
        return super().get_queryset().filter(participants=self.request.user,visibility=True)

class PackageDetail(LoginRequiredMixin,generic.DetailView):
    model = models.Package

    def get_queryset(self):
        package_start_date = get_object_or_404(models.Package,id=self.kwargs.get('pk')).start_time
        self.package_start_date = str(package_start_date)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["start_date"] = self.package_start_date
        return context


class Participate(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('packages:user_package')

    def get(self, request, *args, **kwargs):
        package = get_object_or_404(models.Package,id=self.kwargs.get('package_id'))
        try:
            models.PackageStudent.objects.create(package=package,student=self.request.user) 
        except IntegrityError:
            messages.warning(self.request,'warning already a participant!')
        return super().get(request, *args, **kwargs)

class Leave(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('packages:package_list_all')
    
    def get(self,request,*args,**kwargs):
        try:
            membership = models.PackageStudent.objects.filter(
                student = self.request.user,
                package__id=self.kwargs.get('package_id')
            )
        except models.PackageStudent.DoesNotExist:
            messages.warning(self.request,'Sorry you are not in this package!')
        else:
            membership.delete()

        return super().get(request,*args,**kwargs)

@login_required(login_url='/accounts/login/')
def UserPackageListResult(request,package_id):
    packagestudent = get_object_or_404(models.PackageStudent,package_id=package_id,student=request.user)
    marks = packagestudent.marks
    return render(request,'packages/user_package_result.html',{'result':marks})

