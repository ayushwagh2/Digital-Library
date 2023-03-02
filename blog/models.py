from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Stream(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category2(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Year(models.Model):
    classof = models.IntegerField() 

    def __str__(self):
        return f"Year {self.classof}"

class Document2(models.Model):
    description = models.CharField(max_length=255, blank=True)
    pdf = models.FileField(upload_to='pdf/', null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='documents')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    favourites = models.ManyToManyField(User, related_name='favourite_documents', default=None, blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE, default=2020)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def get_recommendations_url(self):
        return reverse('show_recommendations', kwargs={'document_id': self.pk})


#---------------------------------FOR CONTACT FORM--------------------------------
from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
