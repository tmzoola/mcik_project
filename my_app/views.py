from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Iqtibos
# Create your views here.

def index(request):
    context = Iqtibos.objects.filter(pk=1)
    return render(request,'my_app/index.html',{'content':context})


def about(request):
    return render(request,'my_app/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:login')
    else:
        form = UserCreationForm()
    return render(request, 'auth_templates/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('my_app:index')  # Replace 'home' with your desired URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'auth_templates/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('my_app:index')