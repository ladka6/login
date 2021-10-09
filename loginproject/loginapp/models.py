from django.db import models

# Create your models here.


class Patient(models.Model):
    username = models.CharField(max_length=264)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField()
    password = models.CharField(max_length=100,)
    confirm_password = models.CharField(max_length=100)
    line1 = models.CharField(max_length=264,)
    city = models.CharField(max_length=264,)
    state = models.CharField(max_length=264,)
    pincode = models.IntegerField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.first_name + " " + self.last_name

class Doctor(models.Model):
    username = models.CharField(max_length=264)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    line1 = models.CharField(max_length=264,)
    city = models.CharField(max_length=264, )
    state = models.CharField(max_length=264,)
    pincode = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.first_name + " " + self.last_name

