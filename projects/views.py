from django.shortcuts import render, redirect, get_object_or_404
from .models import Projects
from .forms import ProjectsForm
# Create your views here.


def add_projects(request):
    if request.method == 'POST':
        projects_form = ProjectsForm(request.POST, request.FILES)
        if projects_form.is_valid():
            projects_form.save()
            return redirect('projects:all_projects')
    else:
        projects_form = ProjectsForm()
    return render(request, 'projects/add_projects.html', {'projects_form': projects_form})


def all_projects(request):
    projects_list = Projects.objects.order_by('-created_at')
    return render(request, 'projects/all_projects.html', {'projects_list': projects_list})


def projects_detail(request, pk):
    projects = get_object_or_404(Projects, pk=pk)
    return render(request, 'projects/projects_detail.html', {'projects': projects})


def delete_projects(request, pk):
    projects = get_object_or_404(Projects, pk=pk)
    projects.photo.delete()
    projects.delete()
    return redirect('projects:all_projects')
