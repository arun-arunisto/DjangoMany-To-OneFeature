from django.shortcuts import render, redirect
from .models import Department, Student
from .forms import DeptForm, StuForm
# Create your views here.
def home(request):
    return render(request, 'index.html')

def department(request):
    dept = Department.objects.all()
    return render(request, 'department.html', {'departments':dept})

def create_dept(request):
    form = DeptForm()
    if request.method == 'POST':
        form = DeptForm(request.POST)
        if form.is_valid():
            dept = Department(name=form.cleaned_data['name'])
            dept.save()
            return redirect('department')
    return render(request, 'dept_form.html', {'form':form})

def del_dept(request, pk):
    Department.objects.filter(id=pk).delete()
    return redirect('department')

def student(request):
    stu = Student.objects.all()
    return render(request, 'student.html', {'students':stu})

def stu_create(request):
    form = StuForm()
    if request.method == 'POST':
        form = StuForm(request.POST)
        if form.is_valid():
            stu = Student(name=form.cleaned_data['name'],
                          semester=form.cleaned_data['semester'],
                          course=form.cleaned_data['course'],
                          address=form.cleaned_data['address'],
                          department=form.cleaned_data['department'])
            stu.save()
            return redirect('student')
    return render(request, 'stu_form.html', {'form':form})

def del_stu(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('student')