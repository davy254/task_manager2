from django.urls import path
from . import views


urlpatterns = [
    path('',  views.home, name="home"),
    path("projects/", views.project_list, name="project-list"),
    path("projects/create/", views.create_project, name="create-project"),
    path("projects/<slug:slug>/", views.project_details,  name="project-details"),
    path("projects/<slug:slug>/update/", views.update_project, name="update-project"),
    path("projects/<slug:slug>/delete/", views.delete_project, name="delete-project"),
    
]