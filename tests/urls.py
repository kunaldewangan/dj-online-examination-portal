from django.urls import path
from . import views
from django.views import generic
app_name = 'tests'

urlpatterns = [
    path('<int:package_id>',views.TestView,name='test'),
    path('successful/',generic.TemplateView.as_view(template_name='tests/test_successful.html'),name='test_successful')
]
