from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import timedelta 
from django.utils import timezone
from django.contrib import admin



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Contact(models.Model):
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Email = models.EmailField(help_text='A valid email address, please.')
    MobileNo = models.IntegerField(default=0)
    def __str__(self):
        return self.FirstName