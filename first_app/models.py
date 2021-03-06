from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length = 256,unique = True)
def __str__(self):
    return self.topic_name

class WebPage(models.Model):
    topic_ref = models.ForeignKey(Topic,on_delete=models.CASCADE )
    name = models.CharField(max_length = 256,unique = True)
    url = models.URLField(unique = True)
def __str__(self):
    return self.name


class AccessRecord(models.Model):
    name_rec = models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date = models.DateField()

def __str__(self):
    return str(self.date)

class Login(models.Model):
    name = models.CharField(max_length = 256)
    email = models.EmailField()
    password = models.CharField(max_length = 12)
def __str__(self):
    return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #additional

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to = "Profile_pic",blank = True)

def __str__(self):
    return self.user.username

class School(models.Model):
    name = models.CharField(max_length = 256)
    principal = models.CharField(max_length=256)
    location = models.CharField( max_length=256)
    def get_absolute_url(self):
        return reverse('first_app:detail',kwargs={'pk':self.pk})
def __str__(self):
    return self.name
class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name = 'students')
def __str__(self):
    return self.name
