
from django.conf.urls import (url,
                              include)
from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import static
from jobs import views as job_views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',TemplateView.as_view(template_name='jobs/job_home.html'),name='job_home'),
    url(r'^$',job_views.job_home,name='job_home'),
    # url(r'blog/',TemplateView.as_view(template_name='blog/blog_home.html'),name='job_home'),
    # url(r'^jobs/',include('jobs.urls')),
    url(r'^blogs/',include('blog.urls')),
    # url(r'',job_home,name='job_home'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
