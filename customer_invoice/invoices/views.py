from django.shortcuts import render
from .models import Invoice, InvoiceItem

from xhtml2pdf import pisa
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template


def index(request):
    return render(request, 'index.html')

def schedule1(request):
    context = {
            "company_name" : "wfd",
            "invoice_number":"234345",
            "invoice_date":"2024/09/28",
            "customer_name":"Beku",
            "customer_address":"Cherag Ali",
            "item":"socuso ocoo",
            "title": "Schedule 1"
        }
    response = render_to_pdf("schedule1.html", context)


    if response.status_code == 404:
        raise HTTP404("Invoice not found")

    filename = f"schedule1.pdf"
    content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content

    return response




def schedule5(request):
    context = {
            "company_name" : "wfd",
            "invoice_number":"234345",
            "invoice_date":"2024/09/28",
            "customer_name":"Beku",
            "customer_address":"Cherag Ali",
            "item":"socuso ocoo",
            "title": "Schedule 5"
        }
    response = render_to_pdf("schedule5.html", context)


    if response.status_code == 404:
        raise HTTP404("Invoice not found")

    filename = f"schedule5.pdf"
    content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content

    return response


def it10bb(request):
    context = {
            "company_name" : "wfd",
            "invoice_number":"234345",
            "invoice_date":"2024/09/28",
            "customer_name":"Beku",
            "customer_address":"Cherag Ali",
            "item":"socuso ocoo",
            "title": "IT-10 BB (2023)"
        }
    response = render_to_pdf("it10bb.html", context)


    if response.status_code == 404:
        raise HTTP404("Invoice not found")

    filename = f"it10bb.pdf"
    content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content

    return response



def it10b(request):
    context = {
            "company_name" : "wfd",
            "invoice_number":"234345",
            "invoice_date":"2024/09/28",
            "customer_name":"Beku",
            "customer_address":"Cherag Ali",
            "item":"socuso ocoo",
            "title": "IT-10 B (2023)"
        }
    response = render_to_pdf("it10b.html", context)


    if response.status_code == 404:
        raise HTTP404("Invoice not found")

    filename = f"it10b.pdf"
    content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content

    return response



    
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    return HttpResponse(result.getvalue(), content_type='application/pdf')