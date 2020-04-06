from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('punch/', views.punch, name='punch'),
    path('on_work/', views.on_work, name='on_work'),
    path('off_work/', views.off_work, name='off_work'),
]