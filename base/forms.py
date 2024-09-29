from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['judul', 'deskripsi', 'complete']
        widgets = {
            'judul': forms.TextInput(attrs={
                'class': 'border border-gray-300 p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan judul'
            }),
            'deskripsi': forms.Textarea(attrs={
                'class': 'border border-gray-300 p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan deskripsi'
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'focus:ring-blue-500 relative right-[472px]'
            }),
        }
