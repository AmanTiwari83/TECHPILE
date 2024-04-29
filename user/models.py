from django.db import models


#Create your models here.

class category(models.Model):
    cname=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.cname
class signup(models.Model):
    enroll=models.CharField(max_length=200,null=True)
    name=models.CharField(max_length=100,null=True)
    apply=models.CharField(max_length=100,null=True)
    college=models.TextField(null=True)
    course=models.TextField(null=True)
    year=models.TextField(null=True)
    contact=models.IntegerField(null=True)
    email=models.CharField(max_length=100,null=True)
    date=models.DateField(null=True)
class contactus(models.Model):
    name=models.CharField(max_length=100,null=True)
    contact=models.IntegerField(null=True)
    email=models.CharField(max_length=200,null=True)
    message=models.TextField(null=True)

class feed(models.Model):
    name=models.CharField(max_length=100,null=True)
    picture=models.ImageField(upload_to='static/abc/',null=True)
    college=models.TextField(null=True)
    feedback=models.TextField(null=True)

class imagegallery(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='static/igallery/',null=True)
    idate=models.DateField(null=True)

class videogallery(models.Model):
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    vlink=models.TextField(null=True)
    date=models.DateField(null=True)

class placements(models.Model):
    image=models.ImageField(upload_to='static/placement/',null=True)
    name=models.CharField(max_length=200,null=True)
    college=models.TextField(null=True)
    company=models.CharField(max_length=300,null=True)
    fyear=models.IntegerField(null=True)
    syear = models.IntegerField(null=True)

class coursecategory(models.Model):
    image=models.ImageField(upload_to='static/courses',null=True)
    course=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.course


class courses(models.Model):
    picture=models.ImageField(upload_to='static/courses/',null=True)
    coursecategory=models.ForeignKey(coursecategory,on_delete=models.CASCADE,null=True)
    link=models.CharField(max_length=200,null=True)






