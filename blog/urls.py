
from django.conf.urls import (url,
                              include)
from . import views as blog_views

urlpatterns = [

    url(r'^$',blog_views.blog_home,name='blog_home'),
# url(r'^(?P<post_id>\d+)/$',blog_views.blog_post,name="blog_home"),
    url(r'^(?P<blog_id>\d+)/$',blog_views.blog_details,name='blog_details'),


]
