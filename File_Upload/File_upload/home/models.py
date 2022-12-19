from django.db import models

# Create your models here.
class File(models.Model):
    my_file = models.FileField()

    def __str__(self):
        return self.my_file.name