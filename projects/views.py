from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Photo
from .forms import ProjectForm, PhotoFormSet
import matplotlib.pyplot as plt
from django.http import HttpResponse
from collections import Counter
import io

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

def work_metrics_chart(request):
    # Get work type counts
    work_types = Project.objects.values_list("type_of_work", flat=True)
    work_count = dict(Counter(work_types))

    labels = list(work_count.keys())
    sizes = list(work_count.values())

    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=["#4BA3F0", "#76C2AF", "#F4A261", "#2A9D8F", "#E76F51"])
    ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle

    # Save image to a buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)  # Close figure to free memory
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")
