from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'finished']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'finished':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'dd/mm/yyyy h:m:s'}),
        }