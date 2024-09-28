from django.shortcuts import render
from .models import Invoice, InvoiceItem

def print_invoice(request):
    invoice = Invoice.objects.get(id=1)  # Replace with the actual invoice ID
    items = InvoiceItem.objects.filter(invoice=invoice)
    return render(request, 'invoice.html', {'invoice': invoice, 'items': items})


