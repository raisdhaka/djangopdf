from django.urls import path
from . import views

urlpatterns = [
    path('', views.print_invoice, name='print_invoice'),
]