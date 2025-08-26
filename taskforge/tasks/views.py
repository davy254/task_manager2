from django.shortcuts import render
from .models import Project
from django.core.paginator import Paginator

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


def project_details(request, project_id):
    """"render the details of a project."""
    project = Project.objects.get(id= project_id)
    context = {
        "project": project
    }
    return render(request, "tasks/project_details.html", context)

