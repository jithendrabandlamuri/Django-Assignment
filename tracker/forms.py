from django import forms
from .models import Task

class Add_Task(forms.ModelForm):
    class Meta:
        model=Task
        fields=('add_task','author','Progress')
        widgets={
            'add_task':forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'user','type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'Progress':forms.TextInput(attrs={'class':'form-control'}),
        }