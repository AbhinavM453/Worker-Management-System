from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class user(models.Model):
    UName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    Address = models.CharField(max_length=250)
    Contact = models.CharField(max_length=100)
    Image = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class worker(models.Model):
    WName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    DOB = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    Image = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class feedback(models.Model):
    date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class service(models.Model):
    SName = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    WORKER = models.ForeignKey(worker,on_delete=models.CASCADE,default=1)

class ratings(models.Model):
    date = models.CharField(max_length=100)
    Ratings = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    WORKER = models.ForeignKey(worker,on_delete=models.CASCADE,default=1)

class complaints(models.Model):
    date = models.CharField(max_length=100)
    complaints = models.CharField(max_length=250)
    replay = models.CharField(max_length=100)
    replay_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class servicerequest(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    SERVICE = models.ForeignKey(service, on_delete=models.CASCADE, default=1)







