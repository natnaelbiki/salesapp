from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
# Add custom fields if needed
    pass


# Create your models here.
class Sale(models.Model):
       PRODUCT_CHOICES = [
           ('tiff', 'Tiff'),
           ('bekelo', 'Bekelo'),
           ('boye', 'Boye'),
       ]

       PAYMENT_METHOD_CHOICES = [
           ('cash', 'Cash'),
           ('transfer', 'Transfer'),
           ('debit', 'Debit'),
       ]

       customer_name = models.CharField(max_length=100)
       product_name = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
       quantity = models.IntegerField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
       sale_date = models.DateField(auto_now_add=True)
       sold_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
       payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
       payment_date = models.DateField(null=True, blank=True)

       def __str__(self):
           return f"{self.customer_name} bought {self.product_name} on {self.sale_date}"