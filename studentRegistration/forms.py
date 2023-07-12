from django import forms
from .models import Student, Department

class DeptForm(forms.Form):
    name = forms.CharField(max_length=50)

class StuForm(forms.Form):
    name = forms.CharField(max_length=100)
    semester = forms.IntegerField()
    course = forms.CharField(max_length=50)
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
