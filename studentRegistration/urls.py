from django.urls import path
from .views import home, department, student

urlpatterns = [
    path('',home, name='home'),
    path('department/', department, name='department'),
    path('student/', student, name='student')
]