from django import forms
from .models import TodoList

class TaskForm(forms.ModelForm):
    class Meta:
        model=TodoList
        fields=['tasks','done']
    