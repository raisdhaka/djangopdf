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





def itTenB_pdf_function():
    

    html = '<html><body>'


    html += '<h1>IT-10 B (2023)</h1>'
    html += '<h2>Statement of Assets, Liabilities and Expenses</h2>'
    html += '<div class="form-group">'
    html += '<label>Name of the Assessee:</label>'
    html += '<input type="text" id="assessee-name">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>TIN:</label>'
    html += '<input type="text" id="tin">'
    html += '</div>'

    html += '<h3>Sources of fund:</h3>'
    html += '<div class="form-group">'
    html += '<label>1. Total income shown in return:</label>'
    html += '<input type="text" id="total-income">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>2. Tax Exempted Income:</label>'
    html += '<input type="text" id="tax-exempted-income">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>3. Receipt of Gift and others:</label>'
    html += '<input type="text" id="receipt-of-gift">'
    html += '</div>'

    html +="<h3>Particular of assets located in Bangladesh:</h3>"
    html += '<div class="form-group">'
    html += '<label>4. Business capital in Partnership Firm:</label>'
    html += '<input type="text" id="business-capital">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>5. Motor car(s) (cost value):</label>'
    html += '<input type="text" id="motor-car-value">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>6. Non-agricultural property/land/building:</label>'
    html += '<input type="text" id="non-agri-property">'
    html += '</div>'

    html += '<h3>Financial assets:</h3>'
    html += '<div class="form-group">'
    html += '<label>7. Fixed Deposit/Term Deposit:</label>'
    html += '<input type="text" id="fixed-deposit">'
    html += '</div>'

    html += '<div class="form-group">'
    html += ' <label>8. Provident Fund or Other Fund:</label>'
    html += '<input type="text" id="provident-fund">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>9. Other investment:</label>'   
    html += '<input type="text" id="other-investment">'
    html += '</div>'

    html += '<h3> <h3>Assets located outside of Bangladesh:</h3></h3>'
    html += '<div class="form-group">'
    html += '<label>10. Furniture and electronic items:</label>'   
    html += '<input type="text" id="furniture-electronics">'
    html += '</div>'

    html += '<div class="form-group">'
    html += '<label>11. Other assets:</label>'
    html += '<input type="text" id="other-assets">'
    html += '</div>'

  
    html += '<div class="form-group">'
    html += '<label>Date:</label>'
    html += '<input type="text" id="date">'
    html += '</div>'


    html += '<p>I declare that to the best of my knowledge and belief the information given in this IT-10B (2023) herewith are correct and complete.</p>'

    html += '<div class="form-group">'
    html += '<label>Name of Assessee and Signature:</label>'
    html += '<input type="text" id="signature">'
    html += '</div>'
    

  
    html += '</body></html>'
    
    result = pisa.CreatePDF(html)
    return result


def print_itTenB(request):

    if request.method == 'POST':
        result = itTenB_pdf_function()
        if result.err:
            return HttpResponse('Error generating PDF: %s' % result.err)
        response = HttpResponse(content_type='application/pdf')
        response.write(result.dest.getvalue())
        return response

        # return it10b_pdf_function()
     
    
    return render(request, 'itTenB.html')

    
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if pdf.err:
        return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
    return HttpResponse(result.getvalue(), content_type='application/pdf')