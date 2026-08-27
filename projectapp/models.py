from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Title: {self.name}, Last edited: {self.last_edited.date()}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)
    description =  models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)

