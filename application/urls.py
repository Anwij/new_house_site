from django.urls import path
from .views import (
    add_application,
    all_application,
    application_detail,
    delete_application
)

app_name = 'application'
urlpatterns = [
    # Ваши существующие urlpatterns
    path('add_application/', add_application, name='add_application'),
    path('all_application/', all_application, name='all_application'),
    path('application_detail/<int:pk>/', application_detail, name='application_detail'),
    path('delete_application/<int:pk>/', delete_application, name='delete_application'),
]
