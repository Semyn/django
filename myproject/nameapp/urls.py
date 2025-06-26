from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.show_name, name='show_name'),
]