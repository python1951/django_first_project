from django.db import models

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

# class SiteName(models.Model):
#     site_name = models.CharField(max_length = 256,)
# def __str__(self):
#     return self.site_name
