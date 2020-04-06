from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='task_index'),
    path('index/', views.index, name='task_index'),
    path('add/', views.task_add, name='task_add'),
    path('edit/', views.task_edit, name='task_edit'),
    path('do_edit/', views.do_edit, name='do_edit'),
    path('delete/', views.do_delete, name='do_delete'),
    path('complete/', views.task_complete, name='task_complete'),
    path('do_complete/', views.do_complete, name='do_complete'),
]