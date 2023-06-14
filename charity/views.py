import uuid
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
# Create your views here.

def home(request):
    host = request.get_host()
    

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "20.00",
        "item_name": "donation 1",
        "invoice": str(uuid.uuid4()),
        "notify_url": f'http://{host}{reverse("paypal-ipn")}',
        "return":f'http://{host}{reverse("paypal-reverse")}' ,
        "cancel_return": f'http://{host}{reverse("paypal-cancel")}',
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}

    return render(request,'charity/home.html',context)    