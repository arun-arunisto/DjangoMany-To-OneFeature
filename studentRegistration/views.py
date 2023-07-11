from django.shortcuts import render
from .models import Department, Student

# Create your views here.
def home(request):
    return render(request, 'index.html')

def department(request):
    dept = Department.objects.all()
    return render(request, 'department.html', {'departments':dept})

def student(request):
    stu = Student.objects.all()
    return render(request, 'student.html', {'students':stu})