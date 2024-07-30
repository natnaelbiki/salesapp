from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sale
from .forms import SaleForm


@login_required
def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sale_list.html', {'sales': sales})

@login_required
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sold_by = request.user  # Assign the current user to sold_by field
            if sale.payment_method == 'debit':
                sale.payment_date = form.cleaned_data['payment_date']
                sale.save()
                return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'sales/sale_form.html', {'form': form})