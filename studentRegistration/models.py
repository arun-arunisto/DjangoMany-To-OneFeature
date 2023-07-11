from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - Department'

class Student(models.Model):
    name = models.CharField(max_length=100)
    semester = models.IntegerField()
    course = models.CharField(max_length=50)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'Student name: {self.name}'
