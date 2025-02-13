from django.urls import path
from django.contrib import admin
from . import views
from .views import login_view, signup_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="login"),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path("home/", views.home_view, name="home"),  
    path("tasks/", views.tasks_view, name="tasks"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("tasks/delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("events/", views.events_view, name="events"),
    
]