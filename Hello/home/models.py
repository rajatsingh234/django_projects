from django.db import models

# makemigrations: create changes and store in a file
# migratr: apply the pending changes made by makemigrations

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    phone=models.IntegerField()
    desc=models.TextField()
    date=models.DateField()

    def __str__(self) -> str:
        return f"{self.name} "