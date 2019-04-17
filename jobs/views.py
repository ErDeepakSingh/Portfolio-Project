from django.shortcuts import render
from . import models as job_models
# Create your views here.
def job_home(request):
    jobs=job_models.Job.objects.all()
    return render(request,'jobs/job_home.html',{'jobs':jobs})