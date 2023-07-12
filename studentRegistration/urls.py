from django.urls import path
from .views import home, department, student, create_dept, del_dept, stu_create, del_stu

urlpatterns = [
    path('',home, name='home'),
    path('department/', department, name='department'),
    path('student/', student, name='student'),
    path('create_dept/', create_dept, name='dept_form'),
    path('del_dept/<int:pk>/', del_dept, name='del_dept'),
    path('stu_create/', stu_create, name='stu_create'),
    path('del_stu/<int:pk>/', del_stu, name='stu_delete')
]