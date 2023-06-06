from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Iqtibos
from charity.models import Charity,Donation
from django.db.models import Sum
# Create your views here.

def index(request):
    context = Iqtibos.objects.filter(pk=1)
    charities = Charity.objects.all().order_by('-id')[:3]

    content = {'content':context,
               'charities':charities
               }

    return render(request,'my_app/index.html',content)


def about(request):
    donations = Donation.objects.all()
    person_amount =  donations.count()
    donation_amount = Donation.objects.aggregate(Sum('amount'))['amount__sum']
    charities = Charity.objects.all()
    charity_amount = charities.count()
    
    
    context = {
        'person_amount':person_amount,
        'donation_amount':donation_amount,
        'charity_amount':charity_amount,
        'donations':donations

    }


    return render(request,'my_app/about.html',context=context)

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


