from django.urls import path

from . import views

app_name = 'display'
urlpatterns = [
    path('', views.index, name='index'),
    path('button/', views.button, name='button'),
    path('interval/', views.interval, name='inteval'),
    path('display-name/', views.displayName, name='display-name'),
]
