from django.db import models

class Iqtibos(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class BankAccount(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name
    

