"""online_mcq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

admin.site.site_header = "Online MCQ System"
admin.site.index_title = "MCQ System Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('main/',views.MainPage.as_view(),name='main'),
    path('thanks/',views.ThanksPage.as_view(),name='thanks'),
    path('test/',include('tests.urls', namespace='tests')),
    path('packages/',include('packages.urls',namespace='packages'))
]
