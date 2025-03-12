from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth.views import LogoutView
from .views import login_view, signup_view, delete_account, change_password, update_fontsize, get_fontsize, validate_qr


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="login"),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path("home/", views.home_view, name="home"),  
    path("settings/", views.settings_view, name="settings"),  
    path("tasks/", views.tasks_view, name="tasks"),
    path("tasks/add/", views.add_task, name="add_task"),
    path("tasks/complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path('tasks/delete/<int:user_task_id>/', views.delete_task, name='delete_task'),
    path("events/", views.events_view, name="events"),
    path("events/joinevent/", views.join_event, name="join_event"),
    path("events/leaveevent/", views.leave_event, name="leave_event"),
    path("events/completeevent/", views.complete_event, name="complete_event"),
    path("events/gettasks/<int:event_id>/", views.get_event_tasks, name="get_event_tasks"),
    path('delete-account/', delete_account, name='delete_account'),
    path("change_password/", change_password, name="change_password"),
    path("update-fontsize/", update_fontsize, name="update_fontsize"),
    path("get-fontsize/", get_fontsize, name="get_fontsize"),
    path("term_of_use/",views.terms_view, name="term_of_use"),
    path('logout/', views.logout_view, name='logout'),
    path("shop/", views.shop_view, name="shop"),
    path("shop/buy/<int:item_id>/", views.buy_item, name="buy_item"),
    path('validate/<uuid:token>/', validate_qr, name='validate_qr'),
]