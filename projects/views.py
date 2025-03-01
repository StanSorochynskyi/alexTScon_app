from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Photo
from .forms import ProjectForm, PhotoFormSet

def project_list(request):
    """View to list all projects"""
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    """View to show details of a project along with its photos"""
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def create_project(request):
    """View to create a new project along with multiple photos"""
    if request.method == "POST":
        form = ProjectForm(request.POST)
        formset = PhotoFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            project = form.save()
            photos = formset.save(commit=False)
            for photo in photos:
                photo.project = project
                photo.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
        formset = PhotoFormSet()

    return render(request, 'projects/project_form.html', {'form': form, 'formset': formset})
