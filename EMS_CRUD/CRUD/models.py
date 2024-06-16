from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100,verbose_name="Employee name")
    email=models.EmailField(max_length=277,verbose_name="Employee email")
    role=models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)