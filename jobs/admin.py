from django.contrib import admin
from . import models as Jobs_models

# Register your models here.
admin.site.register(Jobs_models.Job)