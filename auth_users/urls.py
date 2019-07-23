from django.urls import path

from . import views

app_name = 'auth_users'
urlpatterns = [
    path('', views.login, name='index'),
]