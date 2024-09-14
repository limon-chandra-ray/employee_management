from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
