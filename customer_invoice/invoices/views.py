from django.shortcuts import render
from .models import Invoice, InvoiceItem

from xhtml2pdf import pisa
from django.http import HttpResponse
from io import BytesIO


def print_invoice(request):

    if request.method == 'POST':
        company_name = 'wfd'
        invoice_number="234345"
        invoice_date="2024/09/28"
        customer_name="Beku"
        customer_address="Cherag Ali"
        item="socuso ocoo"
        # Generate PDF using xhtml2pdf
        result = generate_pdf_function(company_name, invoice_number, invoice_date, customer_name, customer_address, item)
        if result.err:
            return HttpResponse('Error generating PDF: %s' % result.err)
        response = HttpResponse(content_type='application/pdf')
        response.write(result.dest.getvalue())
        return response


    invoice = Invoice.objects.get(id=1)  # Replace with the actual invoice ID
    items = InvoiceItem.objects.filter(invoice=invoice)
    return render(request, 'invoice.html', {'invoice': invoice, 'items': items})


def generate_pdf_function(company_name, invoice_number, invoice_date, customer_name, customer_address, item):
    

    html = '<html><body>'


    html += '<h1 style="text-align:center">Schedule 1</h1'
    html += '<p style="text-align:center">The schedule below shall be filled in if there is income from emplyment</p>'
    html += '<p>a. This part is applicable for employees receiving Salary under Govt. pay scale</p>'
    html += '<p>Name of the Assessee:						#REF!</p>'
    html += '<p style="text-align:right">TIN ..............................</p>'
    
    html += '<table style="border: 1px solid #000">'
    html += '<thead><tr><th width="20">Sl</th><th width="60%">Particulars</th><th>Income Amount</th><th>Tax Exempted Incoome</th><th>Net Taxable Income</th></tr></thead>'
    html += '<tbody>'
    html += '<tr><td>1</td><td>Basic pay</td><td></td><td></td></tr>'
    html += '<tr><td>2</td><td>Arrear Salary (if not included in taxable income earlier)</td><td></td><td></td></tr>'
    html += '<tr><td>3</td><td>Special allowance / Honorarium</td><td></td><td></td></tr>'
    html += '<tr><td>4</td><td>House rent allowance / Telephone</td><td></td><td></td></tr>'
    html += '<tr><td>5</td><td>Medical allowance</td><td></td><td></td></tr>'
    html += '<tr><td>6</td><td>Conveyance allowance</td><td></td><td></td></tr>'
    html += '<tr><td>7</td><td>Festival Allowance</td><td></td><td></td></tr>'
    html += '<tr><td>8</td><td>Allowance for support staff</td><td></td><td></td></tr>'
    html += '<tr><td>9</td><td>Telephone Allowance</td><td></td><td></td></tr>'
    html += '<tr><td>10</td><td>Mobile Allowance Allowance</td><td></td><td></td></tr>'
    html += '<tr><td>11</td><td>Recreation  allowance</td><td></td><td></td></tr>'
    html += '<tr><td>12</td><td>Baishakhi Allowance</td><td></td><td></td></tr>'
    html += '<tr><td>13</td><td>Interest accrued on provident fund</td><td></td><td></td></tr>'
    html += '<tr><td>14</td><td>Entertainment Allowance</td><td></td><td></td></tr>'
    html += '<tr><td>15</td><td>Gratuity</td><td></td><td></td></tr>'
    html += '<tr><td>16</td><td>Others, if any (Education Allowance)</td><td></td><td></td></tr>'
    html += '<tr><td>17</td><td>Total </td><td></td><td></td></tr>'
    html += '</tbody></table>'

    html += '<p>b. This part is applicable for employees other than employees receiving Salary under Govt. pay scale</p>'
    
    html += '<table style="border: 1px solid #000">'
    html += '<thead><tr><th width="20">Sl</th><th width="70%">Particulars</th><th>Income Amount</th><th>Income Amount</th></tr></thead>'
    html += '<tbody>'
    
    html += '<tr><td>1</td><td>Basic pay<td></td><td></td></tr>'
    html += '<tr><td>2</td><td>Allowances<td></td><td></td></tr>'
    html += '<tr><td>3</td><td>Advance / Arrear Salary<td></td><td></td></tr>'
    html += '<tr><td>4</td><td>Gratuity, Annuity, Pension or similar benefits<td></td><td></td></tr>'
    html += '<tr><td>5</td><td>Perquisites<td></td><td></td></tr>'
    html += '<tr><td>6</td><td>Receipt in lieu of or in addition to salary or wages<td></td><td></td></tr>'
    html += '<tr><td>7</td><td>Income from Employees share scheme<td></td><td></td></tr>'
    html += '<tr><td>8</td><td>Accomodation benefits<td></td><td></td></tr>'
    html += '<tr><td>9</td><td>Car benefits<td></td><td></td></tr>'
    html += '<tr><td>10</td><td>Any other benefits provided by employer<td></td><td></td></tr>'
    html += '<tr><td>11</td><td>Employers contribution to recognized provident fund<td></td><td></td></tr>'
    html += '<tr><td>12</td><td>Others, if any ( provide particulars)<td></td><td></td></tr>'
    html += '<tr><td>13</td><td>Total salary received  (aggregate of 1 to 12)<td></td><td></td></tr>'
    html += '<tr><td>14</td><td>Exempted Portion (As per Part 1 of 6th scheduleof  ITA 2023)<td></td><td></td></tr>'
    html += '<tr><td>15</td><td>Total Income from Employment (13-14)<td></td><td></td></tr>'
    html += '</tbody></table>'


  
    html += '</body></html>'
    result = pisa.CreatePDF(html, dest=BytesIO())
    return result


