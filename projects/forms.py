from django import forms
from .models import Project, Photo
from django.forms import inlineformset_factory

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['type_of_work', 'name', 'description']

# Inline formset for managing multiple photos related to a project
PhotoFormSet = inlineformset_factory(Project, Photo, fields=['image', 'caption'], extra=3)
