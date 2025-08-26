from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    """Render the home page."""
    
    return render(request, "tasks/home.html")


def project_list(request):
    """Render the projects on homepage."""
    projects = Project.objects.all()
    
    context = {
        'projects': projects
    }
    return render(request, "tasks/project_list.html", context)


