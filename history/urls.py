from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SessionView.as_view(), name='session_detail'),
    path('character/<int:pk>/', views.CharacterView.as_view(), name='character'),
]