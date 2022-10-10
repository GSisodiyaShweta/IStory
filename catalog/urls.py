from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('story/', views.story, name='story'),
    path('dontshoot/', views.dontshoot, name='dontshoot'),
    path('register/', views.register_request, name='register'),
    path('', name='save_choices'),
]
