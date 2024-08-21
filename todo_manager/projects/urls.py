from django.urls import path
from . import views
from . views import *
# from .views import user_login, user_logout, register

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('project/new/', views.create_project, name='create_project'),
    path('project/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('view_project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('edit_project_title/<int:project_id>/', views.edit_project_title, name='edit_project_title'),
    path('todo/new/<int:project_id>/', views.create_todo, name='create_todo'),
    path('todo/update/<int:pk>/', views.update_todo, name='update_todo'),
    path('todo/delete/<int:pk>/', views.delete_todo, name='delete_todo'),  
    path('todo/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('project/export/<int:project_id>/', views.export_gist, name='export_gist'),
]
