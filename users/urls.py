from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>/', views.any_profile,name='any_profile'),
]