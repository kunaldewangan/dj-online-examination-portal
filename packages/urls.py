from django.urls import path
from . import views
from django.views import generic

app_name = 'packages'

urlpatterns = [
    path('',views.PackageList.as_view(),name='package_list_all'),
    path('my/',views.UserPackageList.as_view(),name='user_package'),
    path('<int:pk>/detail/',views.PackageDetail.as_view(),name='package_detail'),
    path('<int:package_id>/join/',views.Participate.as_view(),name='participate'),
    path('<int:package_id>/leave/',views.Leave.as_view(),name='leave'),
    path('my/<int:package_id>/result',views.UserPackageListResult,name='user_package_result'),
    
]
