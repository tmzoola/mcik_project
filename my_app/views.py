from django.shortcuts import render
from .models import Iqtibos

# Create your views here.

def index(request):
    context = Iqtibos.objects.filter(pk=1)
    return render(request,'my_app/index.html',{'content':context})


def about(request):
    return render(request,'my_app/about.html')