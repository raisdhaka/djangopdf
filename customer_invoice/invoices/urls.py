from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule1/', views.schedule1, name='schedule1'),
    path('schedule5/', views.schedule5, name='schedule5'),
    path('it10bb/', views.it10bb, name='it10bb'),
    path('it10b/', views.it10b, name='it10b'),
]
    