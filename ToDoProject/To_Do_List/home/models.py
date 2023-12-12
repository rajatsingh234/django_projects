from django.db import models
from django.urls import reverse


# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)

    # def get_absolute_url(self):
    #     return reverse('home')
    def __str__(self) -> str:
        return self.task
