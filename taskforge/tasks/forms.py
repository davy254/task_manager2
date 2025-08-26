from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        
        labels = {
            'name': 'Project Name',
            'description': 'Project Description',

        }
        help_texts = {
            'name': 'Enter the name of the project.',
            'description': 'Provide a brief description of the project.',
        }
