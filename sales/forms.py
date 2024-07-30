from django import forms
from .models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer_name', 'product_name', 'quantity', 'price', 'payment_method', 'payment_date']
