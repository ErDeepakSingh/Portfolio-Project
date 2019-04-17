from django.conf.urls import url
from . import views as job_views

urlpatterns=[
    url(r'^$',job_views.job_home,name='job_home')
]