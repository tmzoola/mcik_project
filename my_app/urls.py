from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('counter/',views.counter, name='counter')
]
