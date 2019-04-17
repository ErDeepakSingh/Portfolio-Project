from django.shortcuts import (render,
                              get_object_or_404)
from . import models as blog_models
# Create your views here.
def blog_home(request):
    blogs=blog_models.Blogs.objects.all()
    return  render(request,'blog/blog_home.html',{'blogs':blogs})
def blog_details(request,blog_id=None):
    blog_id = blog_models.Blogs.objects.get(id=blog_id)

    return render(request,'blog/blog_detail.html',{'blog_detail':blog_id})