from django.db import models

# Create your models here.


class Charity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    telegram_link = models.URLField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name
    

class Donation(models.Model):
    donor = models.CharField(max_length=100)
    charity = models.ForeignKey(Charity,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor} , {self.amount} ni  {self.charity.name} ga ehson qildi  sana: {self.donation_date}"