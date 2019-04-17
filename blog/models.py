from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    image=models.ImageField(default='default.png',upload_to='blog_images')
    body=models.TextField(max_length=200)

    def summary(self):
        return self.body[0:50]
    def date_only(self):
        return self.pub_date.strftime('%b %e , %Y')
    def __str__(self):
        return self.title