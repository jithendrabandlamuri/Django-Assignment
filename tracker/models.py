from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    add_task=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    Progress=models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.add_task)+'|'+str(self.author)

    def get_absolute_url(self):
        return reverse('add_t')