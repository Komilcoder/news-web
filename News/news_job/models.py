from django.db import models
from django.contrib.auth.models import User



class News(models.Model):
    description = models.CharField(max_length=300)
    image = models.FileField(upload_to='media', blank=True,null=True)
    body = models.TextField()
    date_time = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.description
    


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')    