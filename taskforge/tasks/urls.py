from django.urls import path
from . import views


urlpatterns = [
    path('',  views.home, name="home"),
    path("projects/", views.project_list, name="project-list"),
    path("projects/<int:project_id>/", views.project_details,  name="project-details"),
    path("projects/create/", views.create_project, name="create-project"),
    path("projects/<int:project_id>/update/", views.update_project, name="update-project"),
]