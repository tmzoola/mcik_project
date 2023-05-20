from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
]
