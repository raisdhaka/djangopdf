from django.urls import path
from . import views

urlpatterns = [
    path('print_invoice/', views.print_invoice, name='print_invoice'),
]