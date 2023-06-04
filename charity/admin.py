from django.contrib import admin
from charity.models import Charity, Donation

# Register your models here.


admin.site.register([Charity,Donation])