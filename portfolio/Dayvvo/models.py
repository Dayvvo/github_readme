from django.db import models


class Forms(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    project_type = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name + ':' + ' ' + self.date_time


class Form(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    project_type = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name + ':' + ' ' + self.date_time

# Create your models here.
