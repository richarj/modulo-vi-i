from django.urls import path
from . import views

app_name = 'smartphone'

urlpatterns = [
    path('', views.home, name='home')
]
