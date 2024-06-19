from django.urls import path
from .views import (
    add_projects,
    all_projects,
    projects_detail,
    delete_projects
)



app_name = 'projects'
urlpatterns = [
    # Ваши существующие urlpatterns
    path('add_projects/', add_projects, name='add_projects'),
    path('all_projects/', all_projects, name='all_projects'),
    path('projects_detail/<int:pk>/', projects_detail, name='projects_detail'),
    path('delete_projects/<int:pk>/', delete_projects, name='delete_projects'),
]
