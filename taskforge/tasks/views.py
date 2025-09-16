from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from django.core.paginator import Paginator
from .forms import ProjectForm

# Create your views here.
def home(request):
    """Render the home page."""
    
    return render(request, "tasks/home.html")


def project_list(request):
    """Render the projects on homepage."""
    projects = Project.objects.all()
    paginator = Paginator(projects, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {
        'projects': projects,
        'page_obj': page_obj
    }
    return render(request, "tasks/project_list.html", context)


def project_details(request, slug):
    """"render the details of a project."""
    project = Project.objects.get(slug=slug)
    context = {
        "project": project
    }
    return render(request, "tasks/project_details.html", context)

def create_project(request):
    """Create a new project."""
    if request.method == "POST":
        # handle form submission tocreate a new project
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        #display a blank form for creating a new project
        form = ProjectForm()
    context = {
            "form": form
        }
    return render(request, "tasks/project_form.html", context)


def update_project(request, slug):
    """Update an existing project."""
    project = get_object_or_404(Project, slug=slug)
    if request.method == "POST":
        # handle form submission to update the project
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            print("Form is valid ✅")
            updated_project = form.save()
            print("Saved:", updated_project.name, updated_project.description, updated_project.slug)
            return redirect('project-details', slug=updated_project.slug)
           
    else:

        form = ProjectForm(instance=project)
    context = {
        "form": form
    }
    return render(request, "tasks/project_form.html", context)


def delete_project(request, slug):
    """Delete a project."""
    project = Project.objects.get(slug=slug)
    if request.method == "POST":
        project.delete()
        return redirect('project-list')
    return render(request, "tasks/project_confirm_delete.html", {"project":project})
    